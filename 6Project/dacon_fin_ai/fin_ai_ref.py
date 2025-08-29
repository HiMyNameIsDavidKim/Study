import re
import os
import pandas as pd
from tqdm import tqdm

import torch

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

test = pd.read_csv('test.csv')

# 객관식 여부 판단 함수
def is_multiple_choice(question_text):
    """
    객관식 여부를 판단: 2개 이상의 숫자 선택지가 줄 단위로 존재할 경우 객관식으로 간주
    """
    lines = question_text.strip().split("\n")
    option_count = sum(bool(re.match(r"^\s*[1-9][0-9]?\s", line)) for line in lines)
    return option_count >= 2


# 질문과 선택지 분리 함수
def extract_question_and_choices(full_text):
    """
    전체 질문 문자열에서 질문 본문과 선택지 리스트를 분리
    """
    lines = full_text.strip().split("\n")
    q_lines = []
    options = []

    for line in lines:
        if re.match(r"^\s*[1-9][0-9]?\s", line):
            options.append(line.strip())
        else:
            q_lines.append(line.strip())
    
    question = " ".join(q_lines)
    return question, options

    # 프롬프트 생성기
def make_prompt_auto(text):
    if is_multiple_choice(text):
        question, options = extract_question_and_choices(text)
        prompt = (
            "당신은 금융보안 전문 AI입니다.\n"
            "아래 객관식 문제에 반드시 맞는 정답 **번호(1~5)만 한 줄로** 출력하세요.\n"
            "해설·설명·선택지 복붙·기타 말 금지. (예시: 정답이 3번이면 '3'만 쓰세요)\n"
            f"질문: {question}\n"
            "선택지:\n"
            f"{chr(10).join(options)}\n\n"
            "정답:"
        )
    else:
        prompt = (
            "당신은 금융보안 전문 AI입니다.\n"
            "아래 주관식 질문에 30자 이내로 한 문장만 간결하게 답하세요.\n"
            "불필요한 해설·인삿말·반복 금지.\n"
            f"질문: {text}\n\n"
            "답변:"
        )
    return prompt


model_name = "EleutherAI/polyglot-ko-5.8b"

# Tokenizer 및 모델 로드 (4bit)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_4bit=True,
    torch_dtype=torch.float16
)

# Inference pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto"
)

def extract_answer_only(generated_text: str, original_question: str) -> str:
    """
    - 객관식: 1~5, 1~9, 2자리(최대 99) 등 번호만 추출 (한글/영어·정답: 등 모든 변종 커버)
    - 주관식: 한 문장, 30자 이내, 앞뒤 기호/공백/줄바꿈/따옴표 삭제
    """
    text = re.split(r"(정답:|답변:|정답은|정답|Answer:|answer:|답:)", generated_text, maxsplit=1)[-1].strip()
    if not text:
        return "미응답"

    is_mc = is_multiple_choice(original_question)

    if is_mc:
        m = re.match(r'^\s*[\(\[]?\s*([1-9][0-9]?)\s*[\)\.번\s\-:)]*', text)
        if m:
            return m.group(1)
        m = re.search(r'정답[은: ]*([1-9][0-9]?)', text)
        if m:
            return m.group(1)
        m = re.search(r'([1-9][0-9]?)\s*번', text)
        if m:
            return m.group(1)
        m = re.search(r'([1-9][0-9]?)\s*[\)\.]', text)
        if m:
            return m.group(1)
        m = re.search(r'\b([1-9][0-9]?)\b', text)
        if m:
            return m.group(1)
        nums = re.findall(r'[1-9][0-9]?', text)
        if nums:
            return nums[0]
        return "0"
    else:
        txt = re.sub(r'["\'\n]', '', text)
        txt = re.sub(r'^\W+|\W+$', '', txt)
        return txt[:30].strip() if len(txt) > 30 else txt.strip()

preds = []

for q in tqdm(test['Question'], desc="Inference"):
    prompt = make_prompt_auto(q)
    output = pipe(prompt, max_new_tokens=128, temperature=0.2, top_p=0.9)
    pred_answer = extract_answer_only(output[0]["generated_text"], original_question=q)
    preds.append(pred_answer)



sample_submission = pd.read_csv('sample_submission.csv')
sample_submission['Answer'] = preds
sample_submission.to_csv('summit.csv', index=False, encoding='utf-8-sig')