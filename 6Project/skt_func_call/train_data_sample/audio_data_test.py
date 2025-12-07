import pandas as pd
import requests
from tqdm import tqdm
import time
import csv
import re
import os
import glob

def predict_audio_queries():
    # train_data_audio_sample_index.csv 파일 읽기
    df = pd.read_csv('./train_data_sample/train_data_audio_sample_index.csv', quoting=csv.QUOTE_MINIMAL)
    print(f"총 {len(df)} 개의 오디오 데이터를 처리합니다.")

    # 결과를 저장할 리스트
    results = []

    # API 엔드포인트
    api_url = "http://localhost:8000/predict_audio"

    # 오디오 파일 경로
    audio_folder = './train_data_sample/audio'

    # 각 오디오 파일에 대해 예측 요청
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing audio files"):
        index = row['Index']
        query = row['Query(한글)']
        label = extract_response(row['LLM Output'])  # 원본 label

        # Index로 시작하는 오디오 파일 찾기
        pattern = os.path.join(audio_folder, f"{index}*.wav")
        matching_files = glob.glob(pattern)

        if not matching_files:
            print(f"Audio file not found for index: {index}")
            predict = "ERROR_FILE_NOT_FOUND"
            stt_text = "ERROR_FILE_NOT_FOUND"
            audio_filename = f"{index}.wav"  # 기본 파일명 설정
        else:
            # 첫 번째 매칭 파일 사용
            audio_path = matching_files[0]
            audio_filename = os.path.basename(audio_path)

            try:
                # 파일을 multipart/form-data로 전송
                with open(audio_path, 'rb') as audio_file:
                    files = {'file': audio_file}

                    # API 호출
                    response = requests.post(api_url, files=files, timeout=60)

                    if response.status_code == 200:
                        # 성공적으로 응답받은 경우
                        predict_result = response.json()

                        # STT 결과와 예측 결과 추출
                        if isinstance(predict_result, dict):
                            # STT 텍스트 추출
                            stt_text = predict_result.get('transcribed_text',
                                      predict_result.get('stt_text',
                                      predict_result.get('transcription', 'STT_NOT_FOUND')))

                            # 예측 결과 추출
                            predict = predict_result.get('prediction',
                                     predict_result.get('llm_output',
                                     predict_result.get('response', str(predict_result))))
                        else:
                            predict = str(predict_result)
                            stt_text = "STT_NOT_AVAILABLE"
                    else:
                        print(f"Error for audio file '{audio_filename}': HTTP {response.status_code}")
                        predict = f"ERROR_HTTP_{response.status_code}"
                        stt_text = f"ERROR_HTTP_{response.status_code}"

            except requests.exceptions.Timeout:
                print(f"Timeout for audio file: {audio_filename}")
                predict = "ERROR_TIMEOUT"
                stt_text = "ERROR_TIMEOUT"
            except requests.exceptions.RequestException as e:
                print(f"Request error for audio file '{audio_filename}': {e}")
                predict = f"ERROR_REQUEST"
                stt_text = f"ERROR_REQUEST"
            except Exception as e:
                print(f"Unexpected error for audio file '{audio_filename}': {e}")
                predict = f"ERROR_UNKNOWN"
                stt_text = f"ERROR_UNKNOWN"

        # 결과 저장
        results.append({
            'Index': index,
            'Query(한글)': query,
            'Audio_File': audio_filename,
            'STT_Text': stt_text,  # STT 결과 추가
            'label': extract_response(label),
            'predict': extract_response(predict)
        })

        # API 과부하 방지를 위한 대기 (오디오 처리는 더 오래 걸릴 수 있으므로)
        time.sleep(0.5)

    # 결과를 DataFrame으로 변환
    result_df = pd.DataFrame(results)

    # CSV 파일로 저장
    output_filename = './train_data_sample/audio_prediction_results.csv'
    result_df.to_csv(output_filename, index=False, encoding='utf-8-sig',
                     quoting=csv.QUOTE_MINIMAL, escapechar=None)
    print(f"결과가 '{output_filename}' 파일에 저장되었습니다.")

    # 간단한 통계 출력
    print(f"\n처리 완료:")
    print(f"- 총 처리된 오디오 파일 수: {len(results)}")
    print(f"- 에러 발생 수: {len([r for r in results if 'ERROR' in str(r['predict'])])}")

    return result_df


def analyze_audio_prediction_results(path):
    # audio_prediction_results.csv 파일 읽기
    df = pd.read_csv(path)

    # label과 predict가 동일한지 확인
    df['is_correct'] = df['label'] == df['predict']

    # STT 정확도 확인 (원본 Query와 STT_Text 비교)
    if 'STT_Text' in df.columns:
        df['is_stt_correct'] = df.apply(lambda row: str(row['Query(한글)']).strip() == str(row['STT_Text']).strip(), axis=1)
    else:
        df['is_stt_correct'] = False

    # 맞은 것과 틀린 것 개수 계산
    correct_count = df['is_correct'].sum()
    incorrect_count = len(df) - correct_count
    total_count = len(df)

    print("=" * 60)
    print("오디오 예측 결과 분석")
    print("=" * 60)
    print(f"전체 데이터 개수: {total_count}")
    print(f"맞은 개수: {correct_count}")
    print(f"틀린 개수: {incorrect_count}")
    print(f"정확도: {correct_count/total_count*100:.2f}%")
    print()

    # STT 결과 통계
    if 'STT_Text' in df.columns:
        stt_error_count = len(df[df['STT_Text'].str.contains('ERROR', na=False)])
        stt_success_count = total_count - stt_error_count

        # STT 정확도 계산 (ERROR가 아닌 것들 중에서)
        stt_valid_df = df[~df['STT_Text'].str.contains('ERROR', na=False)]
        if len(stt_valid_df) > 0:
            stt_correct_count = stt_valid_df['is_stt_correct'].sum()
            stt_accuracy = stt_correct_count / len(stt_valid_df) * 100
            print(f"STT 성공: {stt_success_count}개, STT 실패: {stt_error_count}개")
            print(f"STT 정확도: {stt_correct_count}/{len(stt_valid_df)} ({stt_accuracy:.2f}%)")
        else:
            print(f"STT 성공: {stt_success_count}개, STT 실패: {stt_error_count}개")
            print("STT 정확도: 계산 불가 (모든 STT가 ERROR)")
        print()

    # 틀린 것들의 Index 추출
    incorrect_rows = df[~df['is_correct']]

    if len(incorrect_rows) > 0:
        print("틀린 예측 결과:")
        print("=" * 120)
        if 'STT_Text' in df.columns:
            print("Index | Query(한글) | STT_Text | Audio_File | Label | Predict")
        else:
            print("Index | Query(한글) | Audio_File | Label | Predict")
        print("=" * 120)

        for _, row in incorrect_rows.iterrows():
            index = row['Index']
            query = row['Query(한글)']
            audio_file = row['Audio_File']
            label = row['label']
            predict = row['predict']

            # 출력 길이 제한 (너무 길면 잘라서 표시)
            query_short = query[:20] + "..." if len(query) > 20 else query
            label_short = label[:25] + "..." if len(label) > 25 else label
            predict_short = predict[:25] + "..." if len(predict) > 25 else predict

            if 'STT_Text' in df.columns:
                stt_text = str(row['STT_Text'])
                stt_short = stt_text[:20] + "..." if len(stt_text) > 20 else stt_text
                print(f"{index} | {query_short} | {stt_short} | {audio_file} | {label_short} | {predict_short}")
            else:
                print(f"{index} | {query_short} | {audio_file} | {label_short} | {predict_short}")

        print("=" * 120)
        print(f"틀린 예측의 Index 목록: {list(incorrect_rows['Index'])}")

    else:
        print("모든 예측이 정확합니다!")

    # STT 틀린 결과 추가 출력
    if 'STT_Text' in df.columns:
        print("\n" + "=" * 60)
        print("STT 틀린 결과 분석")
        print("=" * 60)

        # ERROR가 아닌 것들 중에서 틀린 STT 찾기
        stt_valid_df = df[~df['STT_Text'].str.contains('ERROR', na=False)]
        stt_incorrect_rows = stt_valid_df[~stt_valid_df['is_stt_correct']]

        if len(stt_incorrect_rows) > 0:
            print(f"STT 틀린 개수: {len(stt_incorrect_rows)}개")
            print("=" * 100)
            print("Index | 원본 Query | STT 결과 | Audio_File")
            print("=" * 100)

            for _, row in stt_incorrect_rows.iterrows():
                index = row['Index']
                query = str(row['Query(한글)']).strip()
                stt_text = str(row['STT_Text']).strip()
                audio_file = row['Audio_File']

                # 출력 길이 제한
                query_short = query[:30] + "..." if len(query) > 30 else query
                stt_short = stt_text[:30] + "..." if len(stt_text) > 30 else stt_text

                print(f"{index} | {query_short} | {stt_short} | {audio_file}")

            print("=" * 100)
            print(f"STT 틀린 예측의 Index 목록: {list(stt_incorrect_rows['Index'])}")
        else:
            print("모든 STT 결과가 정확합니다!")

    print("=" * 60)


def test_single_audio_file(audio_filename):
    """단일 오디오 파일을 테스트하는 함수"""
    api_url = "http://localhost:8000/predict_audio"
    audio_folder = './train_data_sample/audio'
    audio_path = os.path.join(audio_folder, audio_filename)

    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        return None

    print(f"Testing audio file: {audio_filename}")

    try:
        with open(audio_path, 'rb') as audio_file:
            files = {'file': audio_file}
            response = requests.post(api_url, files=files, timeout=60)

            if response.status_code == 200:
                result = response.json()
                print(f"Prediction result: {result}")
                return result
            else:
                print(f"Error: HTTP {response.status_code}")
                print(f"Response: {response.text}")
                return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def extract_response(generated_text: str) -> str:
    """생성된 텍스트에서 응답 부분을 추출합니다."""
    response = str(generated_text)

    # 1. 맨 앞뒤의 모든 따옴표 제거 (여러 겹 포함)
    response = re.sub(r'^["\'\s]+|["\'\s]+$', '', response)

    # 2. 연속된 따옴표들을 단일 따옴표로 변환 후 제거
    response = re.sub(r'"{2,}', '"', response)  # """" -> "
    response = re.sub(r"'{2,}", "'", response)  # '''' -> '

    # 3. 남은 모든 따옴표 제거
    response = response.replace('"', '').replace("'", '')

    # 4. 앞뒤 공백 제거
    response = response.strip()

    return response


if __name__ == "__main__":
    print("오디오 데이터 테스트 시작")

    # 단일 파일 테스트 예시 (주석 해제하여 사용)
    # test_single_audio_file("0CMVUL_Level3_B.wav")

    # 전체 오디오 파일 예측 실행 (주석 해제하여 사용)
    results = predict_audio_queries()

    # 결과 분석 실행 (주석 해제하여 사용)
    analyze_audio_prediction_results('./train_data_sample/audio_prediction_results.csv')

    print("테스트 코드가 준비되었습니다!")
    print("사용법:")
    print("1. 단일 파일 테스트: test_single_audio_file('파일명.wav')")
    print("2. 전체 파일 테스트: predict_audio_queries()")
    print("3. 결과 분석: analyze_audio_prediction_results('파일경로')")
