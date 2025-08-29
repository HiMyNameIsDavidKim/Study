import pytesseract
from pdf2image import convert_from_path
import os
import logging
import pandas as pd
import re
import glob

# Windows에서 Tesseract 경로 설정
if os.name == 'nt':  # Windows
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Windows에서 poppler 경로 설정 (conda 환경)
POPPLER_PATH = r'C:\Users\USER\.conda\envs\venv\Library\bin'

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def pdf_to_text_with_ocr(pdf_path, dpi=300, language='eng'):
    """
    PDF 파일을 OCR을 사용하여 텍스트로 변환 (txt 파일 저장 없이)

    Args:
        pdf_path (str): PDF 파일 경로
        dpi (int): 이미지 해상도 (기본값: 300)
        language (str): OCR 언어 (기본값: 'eng', 한국어는 'kor')

    Returns:
        str: 추출된 텍스트
    """
    try:
        logger.info(f"PDF 파일 처리 시작: {os.path.basename(pdf_path)}")

        # PDF를 이미지로 변환
        logger.info("PDF를 이미지로 변환 중...")
        pages = convert_from_path(pdf_path, dpi=dpi, poppler_path=POPPLER_PATH)
        logger.info(f"총 {len(pages)} 페이지 발견")

        extracted_text = ""

        # 각 페이지에 대해 OCR 수행
        for i, page in enumerate(pages, 1):
            logger.info(f"페이지 {i}/{len(pages)} OCR 처리 중...")

            # OCR 수행
            page_text = pytesseract.image_to_string(page, lang=language)

            # 결과에 페이지 구분자 추가
            extracted_text += f"\n--- 페이지 {i} ---\n"
            extracted_text += page_text
            extracted_text += "\n\n"

        logger.info(f"OCR 처리 완료 - 추출된 텍스트 길이: {len(extracted_text)} 문자")

        return extracted_text

    except Exception as e:
        logger.error(f"OCR 처리 중 오류 발생: {str(e)}")
        raise

def process_all_cisa_pdfs():
    """
    모든 CISA PDF 파일을 처리하여 하나의 parquet 파일로 합침

    Returns:
        pd.DataFrame: 모든 질문이 합쳐진 데이터프레임
    """
    try:
        # PDF 파일들이 있는 디렉토리
        current_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_dir = os.path.join(current_dir, "AyemunHossain_Isaca-CISA-Dump-Questions-Study-Material")

        # 모든 PDF 파일 찾기
        pdf_pattern = os.path.join(pdf_dir, "*.pdf")
        pdf_files = glob.glob(pdf_pattern)
        pdf_files.sort()  # 파일명 순으로 정렬

        logger.info(f"총 {len(pdf_files)}개의 PDF 파일 발견")
        for pdf_file in pdf_files:
            logger.info(f"- {os.path.basename(pdf_file)}")

        all_questions = []
        question_counter = 1

        # 각 PDF 파일 처리
        for pdf_file in pdf_files:
            logger.info(f"\n{'='*50}")
            logger.info(f"처리 중: {os.path.basename(pdf_file)}")
            logger.info(f"{'='*50}")

            # OCR 수행
            ocr_text = pdf_to_text_with_ocr(
                pdf_file,
                language='eng+kor',
                dpi=300
            )

            # 질문별로 분리하여 파싱
            questions = parse_ocr_text_to_questions(ocr_text, os.path.basename(pdf_file))

            # 질문 번호를 전체적으로 재할당
            for question in questions:
                question['global_question_number'] = question_counter
                question_counter += 1

            all_questions.extend(questions)
            logger.info(f"{os.path.basename(pdf_file)}에서 {len(questions)}개 질문 추출 완료")

        # DataFrame 생성
        df = pd.DataFrame(all_questions)

        # 최종 parquet 파일 저장
        output_path = os.path.join(current_dir, "15_cisa.parquet")
        df.to_parquet(output_path, index=False)

        logger.info(f"\n{'='*50}")
        logger.info(f"모든 처리 완료!")
        logger.info(f"총 {len(all_questions)}개 질문이 {output_path}에 저장됨")
        logger.info(f"{'='*50}")

        return df

    except Exception as e:
        logger.error(f"전체 처리 중 오류 발생: {str(e)}")
        raise

def parse_ocr_text_to_questions(ocr_text, source_file):
    """
    OCR로 추출된 텍스트를 구조화된 질문 리스트로 변환

    Args:
        ocr_text (str): OCR 텍스트
        source_file (str): 소스 파일명

    Returns:
        list: 구조화된 질문 데이터 리스트
    """
    try:
        logger.info("OCR 텍스트 파싱 시작")

        questions = []

        # Question/QUESTION 패턴 모두 지원 (대소문자 무관)
        question_blocks = re.split(r'\n(?=(?:Question|QUESTION) \d+)', ocr_text, flags=re.IGNORECASE)

        for block in question_blocks:
            if not block.strip() or not re.search(r'(?:Question|QUESTION) \d+', block, re.IGNORECASE):
                continue

            parsed_question = parse_single_question(block, source_file)
            if parsed_question:
                questions.append(parsed_question)

        logger.info(f"파싱 완료: {len(questions)}개 질문 추출")
        return questions

    except Exception as e:
        logger.error(f"OCR 텍스트 파싱 중 오류 발생: {str(e)}")
        raise


def parse_single_question(question_block, source_file):
    """
    개별 질문 블록을 파싱하여 구조화된 데이터로 변환

    Args:
        question_block (str): 개별 질문 텍스트 블록
        source_file (str): 소스 파일명

    Returns:
        dict: 구조화된 질문 데이터
    """
    try:
        lines = question_block.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        # 질문 번호 추출 (Question/QUESTION 모두 지원)
        question_num_match = re.search(r'(?:Question|QUESTION) (\d+)', question_block, re.IGNORECASE)
        if not question_num_match:
            return None

        original_question_number = int(question_num_match.group(1))

        # 텍스트 정리 및 구조화
        cleaned_text = clean_ocr_text(question_block)

        return {
            'original_question_number': original_question_number,
            'source_file': source_file,
            'text': cleaned_text,
            'global_question_number': None  # 나중에 할당됨
        }

    except Exception as e:
        logger.warning(f"질문 파싱 중 오류: {str(e)}")
        return None


def clean_ocr_text(text):
    """
    OCR 텍스트를 정리하고 구조화

    Args:
        text (str): 원본 OCR 텍스트

    Returns:
        str: 정리된 텍스트
    """
    # 페이지 구분자 제거
    text = re.sub(r'--- 페이지 \d+ ---', '', text)

    # 질문 번호 제거 (Question/QUESTION 모두 지원)
    text = re.sub(r'(?:Question|QUESTION) \d+\s*', '', text, flags=re.IGNORECASE)

    # OCR 찌꺼기 제거 - 더 포괄적인 패턴들
    # e 6A., eB., e = =C., e OD. 같은 패턴들을 정리 (. 또는 ) 모두 지원)
    text = re.sub(r'e\s*\d*\s*([ABCD][.)])', r'\1', text)  # e 6A. -> A. 또는 e 6A) -> A)
    text = re.sub(r'e\s*([ABCD][.)])', r'\1', text)  # eB. -> B. 또는 eB) -> B)
    text = re.sub(r'e\s*[=\-\s]*([ABCD][.)])', r'\1', text)  # e = =C. -> C. 또는 e = =C) -> C)
    text = re.sub(r'e\s*O\s*([ABCD][.)])', r'\1', text)  # e OD. -> D. 또는 e OD) -> D)
    text = re.sub(r'e_\s*([ABCD][.)])', r'\1', text)  # e_ A. -> A. 또는 e_ A) -> A)

    # 선택지 앞의 기타 불필요한 문자들 정리 (. 또는 ) 모두 지원)
    text = re.sub(r'[=\-\s]*O\s*([ABCD][.)])', r'\1', text)  # = =O D. -> D. 또는 = =O D) -> D)
    text = re.sub(r'[=\-]+\s*([ABCD][.)])', r'\1', text)  # ===A. -> A. 또는 ===A) -> A)
    text = re.sub(r'^\s*[=\-e\s]*([ABCD][.)])', r'\1', text, flags=re.MULTILINE)  # 줄 시작의 잡음

    # 여러 공백을 단일 공백으로
    text = re.sub(r'\s+', ' ', text)

    # 줄바꿈 정리
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    # 구조 요소들 사이에 적절한 줄바꿈 추가 (. 또는 ) 모두 지원)
    text = re.sub(r'([ABCD][.)] [^A-Z]*?)(?=[ABCD][.)])', r'\1\n', text)
    text = re.sub(r'(Correct Answer: [ABCD])', r'\n\1', text)
    text = re.sub(r'(Explanation:)', r'\n\1', text)

    # 마지막 선택지 뒤에 줄바꿈 추가 (. 또는 ) 모두 지원)
    text = re.sub(r'([ABCD][.)] [^C]*?)(\s*Correct Answer)', r'\1\n\2', text)
    text = f'Q: {text.strip()}'

    return text


def test_single_pdf():
    """
    단일 PDF 파일 테스트 함수 - '200 to 300 CISA dumps.pdf' 파일만 처리
    """
    try:
        # PDF 파일 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_dir = os.path.join(current_dir, "AyemunHossain_Isaca-CISA-Dump-Questions-Study-Material")
        test_pdf = os.path.join(pdf_dir, "200 to 300 CISA dumps.pdf")

        # 파일 존재 여부 확인
        if not os.path.exists(test_pdf):
            logger.error(f"파일을 찾을 수 없습니다: {test_pdf}")
            return None

        logger.info(f"테스트 파일: {os.path.basename(test_pdf)}")

        # OCR 수행
        ocr_text = pdf_to_text_with_ocr(
            test_pdf,
            language='eng+kor',
            dpi=300
        )

        # OCR 텍스트 일부 확인
        logger.info("=== OCR 텍스트 샘플 (처음 1000자) ===")
        logger.info(ocr_text[:1000])
        logger.info("=== OCR 텍스트 샘플 끝 ===")

        # Question/QUESTION 패턴 모두 검색
        question_matches = re.findall(r'(?:Question|QUESTION) \d+', ocr_text, re.IGNORECASE)
        logger.info(f"발견된 Question 패턴들: {question_matches[:10]}")  # 처음 10개만

        # 질문별로 분리하여 파싱
        questions = parse_ocr_text_to_questions(ocr_text, os.path.basename(test_pdf))

        # 결과 출력
        logger.info(f"추출된 질문 수: {len(questions)}")

        # 첫 번째 질문 예시 출력
        if questions:
            logger.info("첫 번째 질문 예시:")
            logger.info(f"원본 질문 번호: {questions[0]['original_question_number']}")
            logger.info(f"텍스트 길이: {len(questions[0]['text'])} 문자")
            logger.info("텍스트 내용 (처음 500자):")
            logger.info(questions[0]['text'][:500] + "..." if len(questions[0]['text']) > 500 else questions[0]['text'])

        return questions

    except Exception as e:
        logger.error(f"테스트 중 오류 발생: {str(e)}")
        raise

def main():
    """
    메인 실행 함수 - 모든 CISA PDF 파일을 처리하여 15_cisa.parquet 생성
    """
    try:
        ## 테스트 모드 실행
        # logger.info("단일 PDF 테스트 모드 실행")
        # test_questions = test_single_pdf()
        #
        # if test_questions:
        #     print(f"\n테스트 완료!")
        #     print(f"'200 to 300 CISA dumps.pdf'에서 {len(test_questions)}개 질문이 추출되었습니다.")
        #     print(f"\n처리된 질문들:")
        #     for i, q in enumerate(test_questions[:5], 1):  # 처음 5개만 표시
        #         print(f"{i}. 원본 질문 번호: {q['original_question_number']}")
        #
        # return test_questions

        # 전체 처리를 원할 경우 아래 주석 해제
        result_df = process_all_cisa_pdfs()
        print(f"\n처리 완료!")
        print(f"총 {len(result_df)}개 질문이 15_cisa.parquet 파일로 저장되었습니다.")
        print(f"\n파일별 질문 수:")
        file_counts = result_df['source_file'].value_counts().sort_index()
        for file_name, count in file_counts.items():
            print(f"- {file_name}: {count}개")

    except Exception as e:
        logger.error(f"메인 실행 중 오류: {str(e)}")
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
