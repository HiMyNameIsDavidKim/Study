import pandas as pd
import re

# 포함할 키워드
RAG_KEYWORDS = [
    # Ref1
    '금융 보안', '금융 산업', '사이버 위협', '보안 위협', '보안 대응',
    '온라인 보안', '인터넷 보안',
    '보이스피싱', '악성 소프트웨어', '사이버 침해', '사이버 보안', '사이버 공격',
    '이상금융거래탐지', '랜섬웨어', '개인정보보호', '정보통신법', '전자서명법',
    '악성코드',

    # Ref2
    '신용정보', '신용정보법', '금융위원회',

    # 못찾음
    '전자금융', '금융감독',
    '시스템 보안', '소프트웨어 보안',
    '한국자산관리공사', '여신금융협회',
]

# 제외할 키워드
EXCLUDE_KEYWORDS = [
]

def contains_keyword(text, keywords):
    """텍스트에 키워드가 포함되어 있는지 확인"""
    if pd.isna(text):
        return False
    text_str = str(text).lower()
    return any(keyword.lower() in text_str for keyword in keywords)

def contains_exclude_keyword(text, keywords):
    """텍스트에 제외할 키워드가 포함되어 있는지 확인"""
    if pd.isna(text):
        return False
    text_str = str(text).lower()
    return any(keyword.lower() in text_str for keyword in keywords)

def chunk_text(text, max_chunk_length):
    """텍스트를 지정된 글자 수로 청킹"""
    if pd.isna(text):
        return []

    text_str = str(text)
    cutoff_keyword = '\n같이 보기 \n'
    cutoff_index = text_str.find(cutoff_keyword)
    if cutoff_index != -1:
        text_str = text_str[:cutoff_index]

    # 문장 분리: \n 또는 .으로 분리
    sentences = re.split(r'[\n.]', text_str)

    # 빈 문장 제거 및 공백 제거
    sentences = [s.strip() for s in sentences if s.strip()]

    # 현재 문장이 n글자 미만이면 다음 문장들과 합치기
    merged_sentences = []
    i = 0
    n = 20
    while i < len(sentences):
        current_sentence = sentences[i]
        while len(current_sentence) < n and i + 1 < len(sentences):
            i += 1
            current_sentence += '. ' + sentences[i]
        merged_sentences.append(current_sentence)
        i += 1
    sentences = merged_sentences

    # 글자수 기준으로 청킹
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # 현재 청크에 문장을 추가했을 때의 길이 계산
        potential_chunk = current_chunk + (". " if current_chunk else "") + sentence

        # 최대 길이를 초과하는 경우
        if len(potential_chunk) > max_chunk_length:
            # 현재 청크가 비어있지 않으면 청크에 추가
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = sentence
            else:
                # 단일 문장이 최대 길이를 초과하는 경우 그대로 추가
                chunks.append(sentence)
        else:
            # 최대 길이 내에서 문장 추가
            current_chunk = potential_chunk

    # 마지막 청크 추가
    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def main():
    # 파케이 파일 읽기
    df = pd.read_parquet('wikimedia_wikipedia.parquet')

    print(f"원본 데이터 크기: {df.shape[0]}개")

    # 키워드가 포함된 행만 필터링 (instruction 또는 output에 키워드가 있는 경우)
    filtered_df = df[
        (df['title'].apply(lambda x: contains_keyword(x, RAG_KEYWORDS)) |
         df['text'].apply(lambda x: contains_keyword(x, RAG_KEYWORDS))) &
        ~(df['title'].apply(lambda x: contains_exclude_keyword(x, EXCLUDE_KEYWORDS)) |
          df['text'].apply(lambda x: contains_exclude_keyword(x, EXCLUDE_KEYWORDS)))
    ]

    print(f"키워드 필터링 후 데이터 크기: {filtered_df.shape[0]}개")

    # output 청킹
    chunked_data = []
    for idx, row in filtered_df.iterrows():
        output_chunks = chunk_text(row['text'], 500)  # 500자 기준으로 청킹
        for chunk in output_chunks:
            chunked_data.append({
                'text': chunk
            })

    # DataFrame으로 변환
    chunked_df = pd.DataFrame(chunked_data)

    # Parquet으로 저장
    output_filename = '03_wikimedia_wikipedia.parquet'
    chunked_df.to_parquet(output_filename, index=False)

    print(f"\n청킹된 데이터가 '{output_filename}' 파일로 저장되었습니다.")
    print(f"저장된 청크 개수: {len(chunked_data)}개")

    # 첫 3개만 미리보기로 출력
    print("\n=== 청크 미리보기 ===")
    for i in range(min(10, len(chunked_data))):
        print(f"\n[{i+1}번째 청크]")
        print(chunked_data[i]['text'][:200] + "..." if len(chunked_data[i]['text']) > 200 else chunked_data[i]['text'])
        # 청크의 문장 수 계산
        chunk_sentences = re.split(r'[\n.]', chunked_data[i]['text'])
        chunk_sentence_count = len([s.strip() for s in chunk_sentences if s.strip()])
        print(f"청크 길이: {len(chunked_data[i]['text'])}자 ({chunk_sentence_count}문장)")
        print("-" * 50)

if __name__ == "__main__":
    main()
