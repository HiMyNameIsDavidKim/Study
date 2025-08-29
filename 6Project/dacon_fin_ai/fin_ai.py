import re
import time
from datetime import datetime
import pandas as pd
from tqdm import tqdm

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

file = open(r"C:\Users\USER\security\hf.txt", "r", encoding='UTF8')
data = file.read()
TOKEN = str(data)
file.close()
login(token=TOKEN)

print(f'cuda: ', torch.cuda.is_available())

test = pd.read_csv('test.csv')
TEST_SAMPLE_SIZE = None  # 10문항만 테스트, 전체 테스트시 None

model_name = "LGAI-EXAONE/EXAONE-4.0-1.2B"
THINKING = False

# 시스템 프롬프트 정의
prompt_version = 'v4'
SYSTEM_PROMPTS = {
"multiple_choice": '''
Answer the following financial security questions correctly.

[Rule Enforcement]
1. Answer in Korean.
2. DO NOT answer with commentary or explanations of the questions.
3. DO NOT answer with a system-level explanations.

[Approach the Problem]
1. first, identify the key concept the question is asking about.
2. Review each option one by one, considering the definition and characteristics of the field.

[Output]
One answer number from 1 to 5.
(e.g., '3' if the answer is 3)
''',
"short_answer": '''
Answer the following financial security questions correctly.

[Rule Enforcement]
1. Answer in Korean.
2. DO NOT answer with commentary or explanations of the questions.
3. DO NOT answer with a system-level explanations.
4. HINT: Answer will be scored on cosine similarity of embeddings and keyword recall. Answer in your favor for points.

[Approach the Problem]
1. Start by defining key terms.
2. Describe specific features or procedures step-by-step.
3. Include what's important from a practical perspective.

[Output]
A answer of 100 words or less.
'''
}

# Tokenizer 및 모델 로드 (4bit)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto",
    # load_in_4bit=True,
    # torch_dtype=torch.float16,
)
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    use_fast=True,
)


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


def get_system_prompt(question_type="multiple_choice"):
    """
    질문 유형에 따른 시스템 프롬프트 반환
    Args:
        question_type: "multiple_choice" 또는 "short_answer"
    """
    return SYSTEM_PROMPTS.get(question_type, SYSTEM_PROMPTS["multiple_choice"])


def format_user_question(question, options=None):
    """
    사용자 질문을 포맷팅
    Args:
        question: 질문 텍스트
        options: 선택지 리스트 (객관식인 경우)
    """
    if options:
        formatted = f"질문: {question}\n선택지:\n{chr(10).join(options)}"
    else:
        formatted = f"질문: {question}"
    return formatted


def format_chat_messages(system_prompt, user_question):
    """
    채팅 형식으로 메시지 포맷팅
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]
    return messages


def make_prompt_with_separation(text, custom_system_prompt=None):
    """
    시스템 프롬프트와 사용자 질문을 분리하여 채팅 템플릿 적용
    Args:
        text: 원본 질문 텍스트
        custom_system_prompt: 사용자 정의 시스템 프롬프트 (선택사항)
    """
    if is_multiple_choice(text):
        question, options = extract_question_and_choices(text)
        system_prompt = custom_system_prompt or get_system_prompt("multiple_choice")
        user_question = format_user_question(question, options) + "\n\n정답:"
    else:
        system_prompt = custom_system_prompt or get_system_prompt("short_answer")
        user_question = format_user_question(text) + "\n\n답변:"

    # 채팅 메시지 형식으로 포맷
    messages = format_chat_messages(system_prompt, user_question)

    return messages


# 프롬프트 생성기 (기존 함수 - 호환성 유지)
def make_prompt_auto(text):
    """기존 함수 - 호환성을 위해 유지"""
    return make_prompt_with_separation(text)

# 최종 답변 추출 함수
def extract_final_answer(output_text: str) -> str:
   if "</think>" in output_text:
       return output_text.split("</think>")[-1].strip().split("\n")[0].strip()
   return output_text.strip()


def extract_number_from_answer(answer: str) -> str:
    """
    multiple_choice 답변에서 숫자만 추출하는 함수
    1글자 이상이라면 첫 번째 숫자만 반환
    """
    if len(answer) <= 1:
        return answer

    # 숫자만 추출 (1-5 범위의 첫 번째 숫자)
    import re
    numbers = re.findall(r'[1-5]', answer)
    if numbers:
        return numbers[0]

    # 숫자가 없으면 원래 답변 반환
    return answer


def generate_response(messages):
    """
    응답 생성
    """
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=THINKING,
        temperature=0.7 if not THINKING else 0.6,
        top_p=0.8 if not THINKING else 0.95,
        top_k=20,
    )
    model_inputs = tokenizer(
        [text],
        return_tensors="pt",
        return_token_type_ids=False,
    ).to(model.device)

    # 응답 생성
    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=256 if not THINKING else 2048,
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

    # 생성된 텍스트 디코딩 (공통)
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    if THINKING:
        response = extract_final_answer(response)

    return response


preds = []

# 테스트 데이터 준비
if TEST_SAMPLE_SIZE is not None:
    test_questions = test['Question'].head(TEST_SAMPLE_SIZE)
    print(f"테스트 모드: {TEST_SAMPLE_SIZE}개 문항만 처리합니다.")
else:
    test_questions = test['Question']
    print(f"전체 모드: {len(test_questions)}개 문항을 처리합니다.")

# 시간 측정 시작
start_time = time.time()
print(f"\n추론 시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 기본 사용법
for q in tqdm(test_questions, desc="Inference"):
    messages = make_prompt_auto(q)
    generated_text = generate_response(messages)

    # multiple_choice인 경우 숫자만 추출
    if is_multiple_choice(q):
        generated_text = extract_number_from_answer(generated_text)

    preds.append(generated_text)

    # 테스트 모드일 때 중간 결과 출력
    if TEST_SAMPLE_SIZE is not None:
        print(f"\n--- 문항 {len(preds)} ---")
        print(f"질문: {q}")
        print(f"생성된 답변: {generated_text}")
        print("-" * 50)

# 시간 측정 완료
end_time = time.time()
elapsed_time = end_time - start_time
questions_processed = len(preds)

print(f"\n총 {questions_processed}개 답변 생성 완료!")
print(f"추론 완료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"총 소요 시간: {elapsed_time:.2f}초 ({elapsed_time/60:.2f}분)")
print(f"문항당 평균 시간: {elapsed_time/questions_processed:.2f}초")


# 결과 저장
sample_submission = pd.read_csv('sample_submission.csv', dtype={'Answer': 'str'})

if TEST_SAMPLE_SIZE is not None:
    # 테스트 모드: 처리한 문항만 업데이트하고 나머지는 기본값 유지
    print(f"테스트 모드: 처음 {len(preds)}개 답변만 업데이트합니다.")
    sample_submission.loc[:len(preds)-1, 'Answer'] = preds
    output_filename = f'submission/submission_{TEST_SAMPLE_SIZE}samples.csv'

    # 514문항 예상 시간 계산
    avg_time_per_question = elapsed_time / questions_processed
    estimated_time_for_514 = avg_time_per_question * 514
    estimated_minutes = estimated_time_for_514 / 60
    estimated_hours = estimated_minutes / 60
    print(f"\n=== 514문항 처리 예상 시간 ===")
    print(f'사용 모델: {model_name}')
    print(f"예상 소요 시간: {estimated_minutes:.1f}분")
else:
    # 전체 모드: 모든 답변 업데이트
    print(f"전체 모드: {len(preds)}개 답변을 업데이트합니다.")
    sample_submission['Answer'] = preds
    now = datetime.now()
    timestamp = now.strftime("%m%d%H%M")  # 월일시분 형식
    short_model_name = model_name.split("/")[-1]  # 모델 이름만 추출
    if THINKING:
        short_model_name += "_thinking"
    output_filename = f'submission/submission_{short_model_name}_p{prompt_version}_{timestamp}.csv'

sample_submission.to_csv(output_filename, index=False, encoding='utf-8-sig')
print(f"결과가 '{output_filename}' 파일로 저장되었습니다.")

# 테스트 모드일 때 결과 미리보기
if TEST_SAMPLE_SIZE is not None:
    print(f"\n=== 처리된 {len(preds)}개 문항 결과 미리보기 ===")
    print(sample_submission.head(TEST_SAMPLE_SIZE)[['Answer']].to_string())
