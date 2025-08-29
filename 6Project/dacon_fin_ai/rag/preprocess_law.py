import pandas as pd
import re
import glob

def preprocess_law_text():
    # '국가법령정보센터'가 포함된 모든 텍스트 파일 찾기
    txt_files = glob.glob("*국가법령정보센터*.txt")

    if not txt_files:
        print("'국가법령정보센터'가 포함된 텍스트 파일을 찾을 수 없습니다.")
        return

    print(f"발견된 파일: {len(txt_files)}개")
    for file in txt_files:
        print(f"  - {file}")

    # 파일들을 순차적으로 처리 (08부터 시작)
    start_number = 8

    for idx, input_file in enumerate(txt_files):
        file_number = f"{start_number + idx:02d}"

        # 법률명에서 파일명 추출 (괄호와 확장자 제거)
        law_base_name = input_file.replace(" (국가법령정보센터).txt", "")
        output_file = f"{file_number}_{law_base_name}.parquet"

        print(f"\n처리 중: {input_file} -> {output_file}")

        # 텍스트 파일 읽기
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {input_file}")
            continue
        except Exception as e:
            print(f"파일 읽기 오류 ({input_file}): {e}")
            continue

        # 결과를 저장할 리스트
        structured_data = []

        # 현재 장 정보를 저장할 변수
        current_chapter = ""

        # 법률명을 파일에서 추출 (첫 번째 줄에서)
        law_name = ""

        # 텍스트를 줄 단위로 분리
        lines = text.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # 빈 줄 건너뛰기
            if not line:
                i += 1
                continue

            # 법률명 추출 (첫 번째 유효한 줄)
            if not law_name and line and not re.match(r'^조문체계도|^생활법령|^위임행정규칙|^관련규제|^\[본조신설|^\[본조삭제', line):
                # 조문이 아니면서 법률명으로 보이는 줄
                if not re.match(r'^\s*제\d+조', line) and not re.match(r'^제\d+장', line):
                    law_name = line
                    i += 1
                    continue

            # 메타데이터 건너뛰기
            if re.match(r'^조문체계도|^생활법령|^위임행정규칙|^관련규제|^\[본조신설|^\[본조삭제', line):
                i += 1
                continue

            # 제X장 패턴 찾기
            chapter_match = re.match(r'^(제\d+장)\s+(.+)', line)
            if chapter_match:
                current_chapter = f"{chapter_match.group(1)} {chapter_match.group(2)}"
                i += 1
                continue

            # 제X조 패턴 찾기
            article_match = re.match(r'^\s*(제\d+조(?:의\d+)?)\s*\(([^)]+)\)\s*(.*)', line)
            if article_match:
                current_article = article_match.group(1)
                current_article_title = article_match.group(2)

                # 조문 전체 내용을 수집
                full_article_content = []

                # 조문 제목 다음에 오는 내용이 있으면 추가
                remaining_content = article_match.group(3).strip()
                if remaining_content:
                    full_article_content.append(remaining_content)

                # 다음 줄들부터 해당 조문의 모든 내용 수집
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()

                    # 다음 조문이나 장이 시작되면 중단
                    if (re.match(r'^\s*제\d+조', next_line) or
                        re.match(r'^제\d+장', next_line)):
                        break

                    # 불필요한 메타데이터는 제외
                    if (re.match(r'^조문체계도|^생활법령|^위임행정규칙|^관련규제|^\[본조신설|^\[본조삭제', next_line) or
                        not next_line):
                        i += 1
                        continue

                    # 유효한 내용이면 추가
                    full_article_content.append(next_line)
                    i += 1

                # 전체 조문 내용 합치기
                if full_article_content:
                    article_text = " ".join(full_article_content)

                    # 메타데이터 제거
                    article_text = re.sub(r'<개정.*?>', '', article_text)
                    article_text = re.sub(r'<신설.*?>', '', article_text)
                    article_text = re.sub(r'<삭제.*?>', '', article_text)
                    article_text = article_text.strip()

                    # 구조화된 텍스트 생성 (장이 있는 경우와 없는 경우 모두 처리)
                    if article_text:
                        if current_chapter:
                            # 장이 있는 경우
                            structured_text = f"{law_name} ({current_chapter} {current_article}) {current_article_title}: {article_text}"
                        else:
                            # 장이 없는 경우
                            structured_text = f"{law_name} ({current_article}) {current_article_title}: {article_text}"
                        structured_data.append({'text': structured_text})
            else:
                i += 1

        # DataFrame 생성 및 파일 저장
        if structured_data:
            df = pd.DataFrame(structured_data)
            df.to_parquet(output_file, index=False)
            print(f"완료: {len(structured_data)}개의 조문이 {output_file}에 저장되었습니다.")

            # 결과 미리보기
            print(f"\n{output_file} 미리보기:")
            for i, row in enumerate(df.head(2).itertuples()):
                print(f"{i+1}. {row.text[:150]}...")
        else:
            print(f"처리할 데이터를 찾을 수 없습니다: {input_file}")

    print(f"\n전체 처리 완료: {len(txt_files)}개 파일 처리됨")

if __name__ == "__main__":
    preprocess_law_text()
