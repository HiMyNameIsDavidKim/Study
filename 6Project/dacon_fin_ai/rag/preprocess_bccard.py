import pandas as pd

# 포함할 키워드
RAG_KEYWORDS = [
    # Ref1
    '금융 보안', '금융 산업', '사이버 위협', '보안 위협', '보안 대응',
    '온라인 보안', '인터넷 보안',
    '보이스피싱', '악성 소프트웨어', '사이버 침해', '사이버 보안', '사이버 공격',
    '이상금융거래탐지', '랜섬웨어', '개인정보보호', '정보통신법', '전자서명법',
    '악성코드',

    # # Ref2
    # '신용정보', '신용정보법', '금융위원회',
    #
    # # 못찾음
    # '전자금융', '금융감독',
    # '시스템 보안', '소프트웨어 보안',
    # '한국자산관리공사', '여신금융협회',
]

# 제외할 키워드
EXCLUDE_KEYWORDS = [
    '비씨카드', 'BC카드', '카드',
    'KT 마이알뜰폰', '행장', 'CEO', '금융그룹',
    '카카오페이', '국민은행', '신한은행', '우리은행', '하나은행', '농협은행', '기업은행', '뱅크', '대구은행',
    '마이데이터', '회사', '윤석열', '모바일 결제', '블라인드 앱',
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

def chunk_text(text, chunk_size):
    """텍스트를 지정된 크기로 청킹하고 100글자 이하인 청크는 제외"""
    if pd.isna(text):
        return []

    text_str = str(text)
    chunks = []

    for i in range(0, len(text_str), chunk_size):
        chunk = text_str[i:i + chunk_size]
        if len(chunk) > 100:
            chunks.append(chunk)

    return chunks

def main():
    # 파케이 파일 읽기
    df = pd.read_parquet('BCCard_BCAI-Finance-Kor-1862K.parquet')

    print(f"원본 데이터 크기: {df.shape[0]}개")

    # 키워드가 포함된 행만 필터링 (instruction 또는 output에 키워드가 있는 경우)
    filtered_df = df[
        (df['instruction'].apply(lambda x: contains_keyword(x, RAG_KEYWORDS)) |
         df['output'].apply(lambda x: contains_keyword(x, RAG_KEYWORDS))) &
        ~(df['instruction'].apply(lambda x: contains_exclude_keyword(x, EXCLUDE_KEYWORDS)) |
          df['output'].apply(lambda x: contains_exclude_keyword(x, EXCLUDE_KEYWORDS)))
    ]

    print(f"키워드 필터링 후 데이터 크기: {filtered_df.shape[0]}개")

    # output 청킹
    chunked_data = []
    for idx, row in filtered_df.iterrows():
        output_chunks = chunk_text(row['output'], 1000)
        for chunk in output_chunks:
            chunked_data.append({
                'text': chunk
            })

    # DataFrame으로 변환
    chunked_df = pd.DataFrame(chunked_data)

    # Parquet으로 저장
    output_filename = '04_BCCard_BCAI-Finance-Kor-1862K.parquet'
    chunked_df.to_parquet(output_filename, index=False)

    print(f"\n청킹된 데이터가 '{output_filename}' 파일로 저장되었습니다.")
    print(f"저장된 청크 개수: {len(chunked_data)}개")

    # 첫 3개만 미리보기로 출력
    print("\n=== 첫 3개 청크 미리보기 ===")
    for i in range(min(3, len(chunked_data))):
        print(f"\n[{i+1}번째 청크]")
        print(chunked_data[i]['text'][:200] + "..." if len(chunked_data[i]['text']) > 200 else chunked_data[i]['text'])
        print(f"청크 길이: {len(chunked_data[i]['text'])}자")
        print("-" * 50)

if __name__ == "__main__":
    main()
