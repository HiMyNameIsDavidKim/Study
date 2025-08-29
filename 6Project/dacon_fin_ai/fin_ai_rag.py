import re
import time
from datetime import datetime
import pandas as pd
from sympy.physics.units import temperature
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from accelerate import Accelerator
import pickle
import os
import hashlib
import faiss

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from huggingface_hub import login

file = open(r"hf.txt", "r", encoding='UTF8')
data = file.read()
TOKEN = str(data)
file.close()
login(token=TOKEN)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'device: ', device)

test = pd.read_csv('test.csv')
TEST_SAMPLE_SIZE = None  # n개 문항만 테스트, 전체 테스트시 None
print_test = False

model_name = "Qwen/Qwen3-4B"
THINKING = False
TEMPERATURE = 0.2  # 0.7 if not THINKING else 0.6
TOP_P = 0.8 if not THINKING else 0.95
TOP_K = 20
MIN_P = 0.0

# 시스템 프롬프트 정의
prompt_version = 'v11'
SYSTEM_PROMPTS = {
"multiple_choice": '''
You are an expert AI in the field of finance and security.
Answer the following financial security questions correctly.

[Rule Enforcement]
1. Answer in Korean.
2. You searched Wikipedia to solve the problem. Review the search results first.

[Approach the Problem]
1.  Accurately understand what the question is asking and the intent of the questioner. Pay particular attention to negative questions such as “Which is appropriate?”, “Which is inappropriate?”, and “Which are all correct?”
2. Clearly extract and organize the key terms, conditions, and constraints necessary for solving the problem.
3-1. Carefully read all four or five options and identify the key points and differences between each option.
3-2. Substitute each option into the problem conditions one by one to determine whether it is true or false, and clearly state the basis for your judgment.
3-3. Eliminate the options that are clearly incorrect first. Carefully filter out options that are only partially correct or contain excessive interpretations.
3-4. Re-examine options that contain extreme expressions (“all,” “always,” “never”), content not mentioned in the text, or logical leaps.
4. Confirm that the selected answer satisfies all the conditions of the question and that you can clearly explain why the other options are incorrect. If you are unsure, use the process of elimination to select the answer with the highest probability of being correct.
5. If a answer information is found in the search results, base your response on that information.
6. If the search results don't contain the answer information, then use only your pre-existing knowledge on financial security.

[Output]
1. 출제자의 의도: Interpretation of the examiner's intent
2. 문제 해결을 위한 핵심 정보: Summary of key information
3. 모든 선택지 풀이: Explanation of each option
4. 최종 답안: One answer number from 1 to 5. (e.g., '3' if the answer is 3)
''',
"short_answer": '''
You are an expert AI in the field of finance and security.
Answer the following financial security questions correctly.

[Rule Enforcement]
1. Answer in Korean.
2. You searched Wikipedia to solve the problem. Review the search results first.

[Approach the Problem]
1. Start by defining key terms.
2. Describe specific features or procedures step-by-step.
3. Include what's important from a practical perspective.
4. If a answer information is found in the search results, base your response on that information.
5. If the search results don't contain the answer information, then use only your pre-existing knowledge on financial security.

[Output]
A answer of 100 words or less.
(HINT: Answer will be scored on cosine similarity of embeddings and keyword recall. Answer in your favor for points.)
'''
}

# RAG
rag_version = 'v7'
RAG_TOP_K = 3
RAG_DOC_NAME = '03-15-n04'
ls_docs = [
    # '01_allganize_financial-mmlu-ko.parquet',  # drop
    # '02_allganize_rag-ko.parquet',  # drop
    '03_wikimedia_wikipedia.parquet',
    # '04_BCCard_BCAI-Finance-Kor-1862K.parquet',  # drop
    '05_mrmoor_cyber-threat-intelligence.parquet',
    '06_Mr-Vicky-01_Security-QnA.parquet',
    '07_sarahwei_cyber_MITRE_attack_tactics-and-techniques.parquet',
    '08_개인정보보호법.parquet',
    '09_신용정보법.parquet',
    '10_전자금융감독규정.parquet',
    '11_전자금융거래법.parquet',
    '12_전자문서 및 전자거래 기본법.parquet',
    '13_전자서명법.parquet',
    '14_정보통신망법.parquet',
    '15_cisa.parquet',
]
RAG_METHOD = 'embedding'  # 'embedding' or 'tfidf'
embedding_model_name = 'Alibaba-NLP/gte-multilingual-base'

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                      # 4비트로 로드
    bnb_4bit_use_double_quant=True,         # 더블 양자화 사용 (메모리 더 절약)
    bnb_4bit_quant_type="nf4",              # 양자화 타입 (nf4 추천)
    bnb_4bit_compute_dtype=torch.float16    # 계산할 때 사용할 데이터 타입
)

# Tokenizer 및 모델 로드 (4bit)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    # torch_dtype="auto",
    quantization_config=bnb_config,  # 4bit
)
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    use_fast=True,
)

# RAG
class SimpleRAG:
    def __init__(self, parquet_files, method='embedding'):
        """RAG 시스템 초기화
        Args:
            parquet_files: 단일 파일명(str) 또는 파일명 리스트(list)
            method: 'embedding' 또는 'tfidf' 방식 선택
        """
        print(f"RAG 시스템 적용 - 방식: {method}")
        self.method = method

        # 파일명을 리스트로 변환
        if isinstance(parquet_files, str):
            file_list = [parquet_files]
        else:
            file_list = parquet_files

        # 모든 문서를 저장할 리스트
        all_documents = []
        all_dataframes = []

        # 각 파일 처리
        for filename in file_list:
            parquet_path = f'rag/{filename}'
            print(f"로딩할 파일: {parquet_path}")

            if filename[:2] in ['01']:
                # parquet 파일 로드
                df = pd.read_parquet(parquet_path)
                all_dataframes.append(df)

                # conversations 컬럼에서 JSON 데이터 파싱
                documents = []
                for conversations_json in df['conversations']:
                    # numpy.ndarray를 list로 변환
                    if hasattr(conversations_json, 'tolist'):
                        conversations_list = conversations_json.tolist()
                    else:
                        conversations_list = conversations_json

                    if isinstance(conversations_list, list) and len(conversations_list) >= 2:
                        human_msg = conversations_list[0].get('value', '') if conversations_list[0].get('from') == 'human' else ''
                        gpt_msg = conversations_list[1].get('value', '') if conversations_list[1].get('from') == 'gpt' else ''
                        if human_msg and gpt_msg:
                            documents.append(f"Q: {human_msg}\nA: {gpt_msg}")

                all_documents.extend(documents)
                print(f"  - {filename}: {len(documents)}개 doc 로드 완료")

            if filename[:2] in ['02']:
                # parquet 파일 로드
                df = pd.read_parquet(parquet_path)
                all_dataframes.append(df)

                # 문서들 추가
                documents = [
                    f"Q: {q}\nA: {a}"
                    for q, a in zip(df['human'], df['answer'])
                ]
                all_documents.extend(documents)
                print(f"  - {filename}: {len(documents)}개 doc 로드 완료")

            if filename[:2] in ['03', '04', '05', '08', '09', '10', '11', '12', '13', '14', '15']:
                # parquet 파일 로드
                df = pd.read_parquet(parquet_path)
                all_dataframes.append(df)

                # 문서들 추가
                documents = []
                for d in df['text']:
                    documents.append(d)
                all_documents.extend(documents)
                print(f"  - {filename}: {len(documents)}개 doc 로드 완료")

            if filename[:2] in ['06']:
                # parquet 파일 로드
                df = pd.read_parquet(parquet_path)
                all_dataframes.append(df)

                # 문서들 추가
                documents = [
                    f"Q: {q}\nA: {a}"
                    for q, a in zip(df['Question'], df['Answer'])
                ]
                all_documents.extend(documents)
                print(f"  - {filename}: {len(documents)}개 doc 로드 완료")

            if filename[:2] in ['07']:
                # parquet 파일 로드
                df = pd.read_parquet(parquet_path)
                all_dataframes.append(df)

                # 문서들 추가
                documents = [
                    f"Q: {q}\nA: {a}"
                    for q, a in zip(df['question'], df['answer'])
                ]
                all_documents.extend(documents)
                print(f"  - {filename}: {len(documents)}개 doc 로드 완료")

        # 전체 데이터프레임 합치기
        if all_dataframes:
            self.df = pd.concat(all_dataframes, ignore_index=True)
        else:
            raise ValueError("로드할 수 있는 파일이 없습니다.")

        # 전체 문서 리스트
        self.documents = all_documents

        if self.method == 'embedding':
            self._init_embedding_model()
        elif self.method == 'tfidf':
            self._init_tfidf_model()
        else:
            raise ValueError("method는 'embedding' 또는 'tfidf' 중 하나를 선택해주세요.")

        print(f"RAG 시스템 초기화 완료. 문서 수: {len(self.documents)}, 방식: {self.method}")

    def _get_cache_key(self, files_list, model_name):
        """캐시 키 생성 (파일 목록과 모델명 기반)"""
        # 파일 목록을 정렬하여 일관성 확보
        sorted_files = sorted(files_list)
        cache_string = f"{sorted_files}_{model_name}"
        return hashlib.md5(cache_string.encode()).hexdigest()

    def _save_embedding_cache(self, cache_key, embeddings, documents):
        """임베딩 결과를 캐시 파일로 저장"""
        cache_dir = "rag/cache"
        os.makedirs(cache_dir, exist_ok=True)

        cache_data = {
            'embeddings': embeddings,
            'documents': documents,
            'model_name': embedding_model_name,
            'timestamp': datetime.now().isoformat()
        }

        cache_file = os.path.join(cache_dir, f"embedding_cache_{cache_key}.pkl")
        with open(cache_file, 'wb') as f:
            pickle.dump(cache_data, f)
        print(f"임베딩 캐시 저장 완료: {cache_file}")

    def _load_embedding_cache(self, cache_key):
        """캐시 파일에서 임베딩 결과 로드"""
        cache_dir = "rag/cache"
        cache_file = os.path.join(cache_dir, f"embedding_cache_{cache_key}.pkl")

        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)

                # 모델명이 일치하는지 확인
                if cache_data.get('model_name') == embedding_model_name:
                    print(f"임베딩 캐시 로드 완료: {cache_file}")
                    print(f"캐시 생성 시간: {cache_data.get('timestamp')}")
                    return cache_data['embeddings'], cache_data['documents']
                else:
                    print("캐시된 모델명이 다릅니다. 새로 생성합니다.")
                    return None, None
            except Exception as e:
                print(f"캐시 로드 실패: {e}. 새로 생성합니다.")
                return None, None
        return None, None

    def _init_embedding_model(self):
        """임베딩 모델 초기화 (캐싱 기능 포함)"""
        # 허깅페이스 임베딩 모델 로드
        print("허깅페이스 임베딩 모델 로딩 중...")

        # Accelerator 초기화
        self.accelerator = Accelerator()

        self.embedding_model = SentenceTransformer(
            embedding_model_name,
            trust_remote_code=True,
            device=device,
        )
        print("임베딩 모델 로드 완료!")

        # 캐시 키 생성 (파일 목록과 모델명 기반)
        file_list = ls_docs if isinstance(ls_docs, list) else [ls_docs]
        cache_key = self._get_cache_key(file_list, embedding_model_name)

        # 캐시에서 임베딩 로드 시도
        print("임베딩 캐시 확인 중...")
        cached_embeddings, cached_documents = self._load_embedding_cache(cache_key)

        if cached_embeddings is not None and cached_documents is not None:
            # 문서가 일치하는지 확인
            if len(cached_documents) == len(self.documents) and cached_documents == self.documents:
                self.doc_vectors = cached_embeddings
                print(f"캐시된 임베딩 사용! 문서 수: {len(self.documents)}")
                # 캐시된 임베딩으로도 FAISS 인덱스 생성
                print("캐시된 임베딩으로 FAISS 인덱스 생성 중...")
                # 벡터를 정규화하여 코사인 유사도를 위한 준비
                normalized_vectors = self.doc_vectors / np.linalg.norm(self.doc_vectors, axis=1, keepdims=True)
                self.index = faiss.IndexFlatL2(normalized_vectors.shape[1])
                self.index.add(normalized_vectors.astype('float32'))
                print("FAISS 인덱스 생성 완료!")
                return
            else:
                print("문서 내용이 변경되었습니다. 새로 생성합니다.")

        # 캐시가 없거나 유효하지 않은 경우 새로 생성
        print("문서 임베딩 생성 중...")

        # 배치 단위로 임베딩 생성하여 진행률 표시
        batch_size = 32  # Accelerator 사용으로 배치 크기 증가
        embeddings = []

        # 문서를 배치로 나누어 처리
        total_batches = (len(self.documents) + batch_size - 1) // batch_size

        for i in tqdm(range(0, len(self.documents), batch_size), desc="임베딩 생성", total=total_batches):
            batch_docs = self.documents[i:i+batch_size]

            with torch.no_grad():
                # Accelerator의 device를 활용
                with self.accelerator.device:
                    batch_embeddings = self.embedding_model.encode(
                        batch_docs,
                        convert_to_tensor=True,  # GPU 활용을 위해 tensor로 변환
                        max_length=1024,
                        truncation=True,
                        show_progress_bar=False,  # tqdm과 중복 방지
                        batch_size=len(batch_docs)  # 내부 배치 크기 제한
                    )

                    # GPU 메모리 관리를 위해 CPU로 이동
                    if isinstance(batch_embeddings, torch.Tensor):
                        batch_embeddings = batch_embeddings.cpu().numpy()

                    embeddings.extend(batch_embeddings)

                    # GPU 메모리 정리
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()

        self.doc_vectors = np.array(embeddings)

        # 생성된 임베딩을 캐시에 저장
        print("임베딩 캐시 저장 중...")
        self._save_embedding_cache(cache_key, self.doc_vectors, self.documents)

        # FAISS 인덱스 생성 및 저장
        print("FAISS 인덱스 생성 중...")
        self.index = faiss.IndexFlatL2(self.doc_vectors.shape[1])  # L2 거리 기반 인덱스
        self.index.add(self.doc_vectors)  # 벡터 추가
        print("FAISS 인덱스 생성 완료!")

    def _init_tfidf_model(self):
        """TF-IDF 모델 초기화"""
        print("TF-IDF 벡터라이저 초기화 중...")

        # TF-IDF 벡터라이저 초기화 (한국어 최적화)
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=10000,  # 최대 특성 수
            stop_words=None,     # 한국어 불용어는 별도 처리 필요
            ngram_range=(1, 2),  # 1-gram과 2-gram 사용
            min_df=2,            # 최소 문서 빈도
            max_df=0.95,         # 최대 문서 빈도 (너무 자주 나오는 단어 제외)
            sublinear_tf=True    # 로그 스케일링 적용
        )

        print("문서 TF-IDF 벡터 생성 중...")
        # 모든 문서에 대해 TF-IDF 벡터 생성
        self.doc_vectors = self.tfidf_vectorizer.fit_transform(self.documents)
        print("TF-IDF 벡터 생성 완료!")

    def search(self, query, top_k):
        """쿼리와 관련된 문서 검색"""
        if self.method == 'embedding':
            return self._search_embedding(query, top_k)
        elif self.method == 'tfidf':
            return self._search_tfidf(query, top_k)

    def _search_embedding(self, query, top_k):
        """임베딩 방식으로 문서 검색 (FAISS 사용)"""
        # 쿼리 임베딩 생성 (Accelerator의 device 활용)
        with self.accelerator.device:
            query_vector = self.embedding_model.encode([query], convert_to_tensor=False)

        # FAISS를 사용한 빠른 유사도 검색
        # L2 거리를 코사인 유사도로 변환하기 위해 벡터 정규화
        query_vector = query_vector / np.linalg.norm(query_vector, axis=1, keepdims=True)

        # FAISS 검색 (거리와 인덱스 반환)
        distances, top_indices = self.index.search(query_vector.astype('float32'), top_k)

        # L2 거리를 코사인 유사도로 변환 (정규화된 벡터의 경우 코사인 유사도 = 1 - L2_distance^2 / 2)
        similarities = 1 - distances[0] / 2
        top_indices = top_indices[0]

        # 결과 반환
        results = []
        for i, idx in enumerate(top_indices):
            results.append({
                'document': self.documents[idx],
                'similarity': similarities[i],
                'index': idx
            })

        return results

    def _search_tfidf(self, query, top_k):
        """TF-IDF 방식으로 문서 검색"""
        # 쿼리를 TF-IDF 벡터로 변환
        query_vector = self.tfidf_vectorizer.transform([query])

        # 코사인 유사도 계산
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()

        # 상위 k개 문서 인덱스
        top_indices = np.argsort(similarities)[::-1][:top_k]

        # 결과 반환
        results = []
        for idx in top_indices:
            results.append({
                'document': self.documents[idx],
                'similarity': similarities[idx],
                'index': idx
            })

        return results


# RAG 시스템 초기화 - 파일명 직접 지정
rag_system = SimpleRAG(
    parquet_files=ls_docs,
    method=RAG_METHOD
)

def generate_answer(messages):
    """채팅 템플릿을 사용한 답변 생성"""
    # 채팅 템플릿 적용
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=THINKING,
    )

    # 토크나이징
    model_inputs = tokenizer(
        [text],
        return_tensors="pt",
        return_token_type_ids=False,
    ).to(model.device)

    # 응답 생성
    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=2048,
            temperature=TEMPERATURE,
            top_k=TOP_K,
            top_p=TOP_P,
            min_p=MIN_P,
            do_sample=True,
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

    # 생성된 텍스트 디코딩
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response

def extract_final_answer(answer, question_type):
    """최종 답변 추출"""
    # THINKING 모드에서 </think> 태그 처리
    if "</think>" in answer:
        answer = answer.split("</think>")[-1].strip()
        return answer

    # 선다형 문항 처리
    if question_type == "multiple_choice":
        final_answer_pattern = r"최종\s*답안\s*[:：]\s*(\d+)"
        match = re.search(final_answer_pattern, answer)
        if match:
            return match.group(1)

        # 백업 패턴
        patterns = [
            r"답안\s*[:：]\s*(\d+)",
            r"정답\s*[:：]\s*(\d+)",
            r"답\s*[:：]\s*(\d+)",
            r"^(\d+)$",
            r"선택지\s*(\d+)",
        ]

        for pattern in patterns:
            match = re.search(pattern, answer.strip(), re.MULTILINE)
            if match:
                return match.group(1)

        # 마지막 숫자 추출
        numbers = re.findall(r'\d+', answer)
        return numbers[-1]

    else:
        return answer

def determine_question_type(question):
    """질문 유형 판단"""
    if re.search(r'[1-5]\s+[가-힣]', question) or '1 ' in question or '2 ' in question:
        return "multiple_choice"
    else:
        return "short_answer"

def create_prompt_with_rag(question, question_type):
    """RAG를 사용하여 관련 문서를 포함한 프롬프트 생성"""
    # RAG로 관련 문서 검색
    search_results = rag_system.search(question, top_k=RAG_TOP_K)

    # 검색된 문서들을 컨텍스트로 결합
    context_documents = []
    for i, result in enumerate(search_results, 1):
        context_documents.append(f"[Wikipedia Search Results {i}]\n{result['document']}")

        # temp test
        if print_test:
            print(f'[참고문서 {i}]')
            print(result['document'][:200])
            print(f'유사도: {result["similarity"]:.4f}')

    # 전체 컨텍스트 생성
    reference_context = "\n\n".join(context_documents)

    # 시스템 프롬프트 선택
    system_prompt = SYSTEM_PROMPTS[question_type]

    user_content = f"""    
    [Question]
    {question}
    
    {reference_context}
    """

    # 메시지 구성
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_content
        }
    ]

    return messages

# 메인 실행 부분
def process_test_questions():
    """테스트 질문 처리"""
    # 테스트 데이터 준비
    if TEST_SAMPLE_SIZE is not None:
        test_questions = test['Question'].head(TEST_SAMPLE_SIZE)
        print(f"테스트 모드: {TEST_SAMPLE_SIZE}개 문항만 처리합니다.")
    else:
        test_questions = test['Question']
        print(f"전체 모드: {len(test_questions)}개 문항을 처리합니다.")

    preds = []

    # 시간 측정 시작
    start_time = time.time()
    print(f"\n추론 시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 질문 처리
    for idx, question in enumerate(tqdm(test_questions, desc="Inference")):
        question_type = determine_question_type(question)

        # RAG 적용된 프롬프트 생성
        prompt = create_prompt_with_rag(question, question_type)

        # 답변 생성
        raw_answer = generate_answer(prompt)
        final_answer = extract_final_answer(raw_answer, question_type)

        preds.append(final_answer)

        # 테스트 모드일 때 중간 결과 출력
        if TEST_SAMPLE_SIZE is not None:
            print(f"\n--- 문항 {len(preds)} ---")
            print(f"질문: {question}")
            print(f"생성된 답변: {final_answer}")
            print(f"타입: {question_type}")
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
        output_filename = f'submission/submission_{short_model_name}_rv{rag_version[1:]}_{RAG_DOC_NAME}_pv{prompt_version[1:]}_{timestamp}.csv'

    sample_submission.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"결과가 '{output_filename}' 파일로 저장되었습니다.")

    # 테스트 모드일 때 결과 미리보기
    if TEST_SAMPLE_SIZE is not None:
        print(f"\n=== 처리된 {len(preds)}개 문항 결과 미리보기 ===")
        print(sample_submission.head(TEST_SAMPLE_SIZE)[['Answer']].to_string())

    return sample_submission

if __name__ == "__main__":
    results = process_test_questions()
    print("RAG-enhanced processing completed!")
