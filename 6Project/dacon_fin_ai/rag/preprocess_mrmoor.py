import pandas as pd


def chunk_text(text, chunk_size):
    """텍스트를 지정된 크기로 청킹"""
    if pd.isna(text):
        return []

    text_str = str(text)
    chunks = []

    for i in range(0, len(text_str), chunk_size):
        chunk = text_str[i:i + chunk_size]
        chunks.append(chunk)

    return chunks

def main():
    # 파케이 파일 읽기
    df = pd.read_parquet('mrmoor_cyber-threat-intelligence.parquet')

    # 전체 text 컬럼을 하나의 문자열로 합치기
    all_text = ' '.join(df['text'].astype(str).tolist())
    print(f"전체 텍스트 길이: {len(all_text)}자")

    # 합쳐진 텍스트를 청킹
    chunked_data = []
    chunks = chunk_text(all_text, 2000)

    for chunk in chunks:
        chunked_data.append({
            'text': chunk
        })

    # DataFrame으로 변환
    chunked_df = pd.DataFrame(chunked_data)

    # Parquet으로 저장
    output_filename = '05_mrmoor_cyber-threat-intelligence.parquet'
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
