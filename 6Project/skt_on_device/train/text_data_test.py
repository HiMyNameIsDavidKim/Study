import pandas as pd
import requests
from tqdm import tqdm
import time
import csv
import re

def predict_queries():
    # train_data.csv 파일 읽기 - quoting 옵션을 조정하여 따옴표 문제 해결
    df = pd.read_csv('./train/train_data.csv', quoting=csv.QUOTE_MINIMAL)
    df = df
    print(f"총 {len(df)} 개의 데이터를 처리합니다.")

    # 결과를 저장할 리스트
    results = []

    # API 엔드포인트
    api_url = "http://localhost:8000/predict"
    headers = {"Content-Type": "application/json"}

    # 각 Query(한글)에 대해 예측 요청
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing queries"):
        query = row['Query(한글)']
        index = row['Index']
        label = extract_response(row['LLM Output'])  # 원본 label

        try:
            # POST 요청 데이터
            data = {"query": query}

            # API 호출
            response = requests.post(api_url, headers=headers, json=data, timeout=30)

            if response.status_code == 200:
                # 성공적으로 응답받은 경우
                predict_result = response.json()
                # 예측 결과가 딕셔너리 형태라면 적절히 추출
                if isinstance(predict_result, dict):
                    predict = predict_result.get('prediction', str(predict_result))
                else:
                    predict = str(predict_result)
            else:
                print(f"Error for query '{query}': HTTP {response.status_code}")
                predict = f"ERROR_HTTP_{response.status_code}"

        except requests.exceptions.Timeout:
            print(f"Timeout for query: {query}")
            predict = "ERROR_TIMEOUT"
        except requests.exceptions.RequestException as e:
            print(f"Request error for query '{query}': {e}")
            predict = f"ERROR_REQUEST"
        except Exception as e:
            print(f"Unexpected error for query '{query}': {e}")
            predict = f"ERROR_UNKNOWN"

        # 결과 저장
        results.append({
            'Index': index,
            'Query(한글)': query,
            'label': label,
            'predict': predict
        })

        # API 과부하 방지를 위한 짧은 대기
        time.sleep(0.1)

    # 결과를 DataFrame으로 변환
    result_df = pd.DataFrame(results)

    # CSV 파일로 저장 - 더 강력한 옵션으로 이스케이프 문제 완전 해결
    output_filename = './train/prediction_results.csv'
    result_df.to_csv(output_filename, index=False, encoding='utf-8-sig',
                     quoting=csv.QUOTE_MINIMAL, escapechar=None)
    print(f"결과가 '{output_filename}' 파일에 저장되었습니다.")

    # 간단한 통계 출력
    print(f"\n처리 완료:")
    print(f"- 총 처리된 쿼리 수: {len(results)}")
    print(f"- 에러 발생 수: {len([r for r in results if 'ERROR' in str(r['predict'])])}")

    return result_df


def analyze_prediction_results(path):
    # prediction_results_0.csv 파일 읽기
    df = pd.read_csv(path)

    # label과 predict가 동일한지 확인
    df['is_correct'] = df['label'] == df['predict']

    # 맞은 것과 틀린 것 개수 계산
    correct_count = df['is_correct'].sum()
    incorrect_count = len(df) - correct_count
    total_count = len(df)

    print("=" * 60)
    print("예측 결과 분석")
    print("=" * 60)
    print(f"전체 데이터 개수: {total_count}")
    print(f"맞은 개수: {correct_count}")
    print(f"틀린 개수: {incorrect_count}")
    print(f"정확도: {correct_count/total_count*100:.2f}%")
    print()

    # 틀린 것들의 Index 추출
    incorrect_rows = df[~df['is_correct']]

    if len(incorrect_rows) > 0:
        print("틀린 예측 결과:")
        print("=" * 60)
        print("Index | Query(한글) | Label | Predict")
        print("=" * 60)

        for _, row in incorrect_rows.iterrows():
            index = row['Index']
            query = row['Query(한글)']
            label = row['label']
            predict = row['predict']

            # 출력 길이 제한 (너무 길면 잘라서 표시)
            query_short = query[:30] + "..." if len(query) > 30 else query
            label_short = label[:40] + "..." if len(label) > 40 else label
            predict_short = predict[:40] + "..." if len(predict) > 40 else predict

            print(f"{index} | {query_short} | {label_short} | {predict_short}")

        print("=" * 60)
        print(f"틀린 예측의 Index 목록: {list(incorrect_rows['Index'])}")

    else:
        print("모든 예측이 정확합니다!")

    print("=" * 60)


def extract_response(generated_text: str) -> str:
    """생성된 텍스트에서 응답 부분을 추출합니다."""
    pattern = r'(?<!")"(?!")'
    response = re.sub(pattern, '""', generated_text)
    response = response.replace('""""', '""').replace('"""', '""')
    return response


if __name__ == "__main__":
    # 예측 실행
    results = predict_queries()
    print("작업이 완료되었습니다!")

    # 결과 분석 실행
    analyze_prediction_results('./train/prediction_results_without_type.csv')
