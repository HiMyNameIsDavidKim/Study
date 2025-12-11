import pandas as pd
import random
from typing import List, Dict
from itertools import combinations

class STTDataAugmenter:
    def __init__(self):
        # STT 오류 패턴 정의
        self.phonetic_errors = {
            '베를린': ['배를린', '벨린', '베린'],
            '자그레브': ['자그레은', '자그랩', '자그렙'],
            '룸푸르': ['룸프로', '룸푸로'],
            '쿠알라': ['쿠알라', '쿠알라'],
            '도쿄': ['토교', '도교'],
            '워르소': ['워소', '와르소'],
            '하얼빈': ['하을빈', '하얼민'],
            '마르세유': ['마르세이', '마세유'],
            '앤트워프': ['엔트워프', '안트워프'],
            '산티아고': ['산디아고', '산타아고'],
            '아부다비': ['아부다미', '아부타비'],
            '나이로비': ['나이로미', '나로비'],
            '자카르타': ['자까르타', '자카타', '자까타'],
            '멜버른': ['멜번', '멜본', '멜블런'],
            '나폴리': ['나뽈리', '나폴린', '나뽈린'],
            '슈투트가르트': ['슈트트가르트', '슈투트가르드', '슈트투트가르트'],
            '카이로': ['카이루', '카일로'],
            '루체른': ['루첸', '루체론'],
            '포항': ['포항', '포한'],
            '남원': ['남원', '남운'],
            '케이프타운': ['케이프타운', '케이프다운', '케이프탄'],
            '강릉': ['강능', '강릉이'],
            '오사카': ['오사까', '오사가'],
            '퀘벡': ['궤벡', '퀘백'],
            '앙카라': ['앙카라', '앙까라', '안카라'],
            '뉴델리': ['뉴델리', '뉴델리이', '뉴델린'],
            '시드니': ['시드니이', '씨드니', '시드닌'],
            '창춘': ['창춘', '창츈'],
            '우한': ['우한', '우헌', '우환'],
            '베이징': ['뻬이징', '베이찡', '베이진'],
            '오클랜드': ['오클렌드', '오클란드', '오클렝드'],
            '하노이': ['하노이이', '하노이', '하노'],
            '타슈켄트': ['타슈켄', '타슈켄투', '타슈켄드'],
            '카사블랑카': ['까사블랑카', '카사블란카'],
            '푸켓': ['뿌껫', '푸캣', '푸겟'],
            '치앙마이': ['치앙마', '치안마이'],
            '리우데자네이루': ['리우데자네루', '리우데자네이로', '리오데자네이루'],
            '블라디보스토크': ['블라디보스톡', '블라디보스또크'],
            '하바나': ['아바나', '하바너'],
            '상하이': ['샹하이', '쌍하이'],
            '여수': ['여슈', '여쑤'],
            '순천': ['순쳔', '순천이'],
            '군산': ['군싼', '군샨'],
            '용산구': ['용상구', '용산'],
            '전주': ['전쭈', '전쥬']
        }

        self.word_errors = {
            '청정': ['정정', '청점', '천정'],
            '알려': ['알려', '일려', '알어'],
            '날씨': ['날기', '날세', '낼씨'],
            '어때': ['없대', '어떄', '어대'],
            '공기질': ['공기지', '공질', '공기잘'],
            '모니터링': ['모니터', '모니토링', '모니덜링'],
            '볼륨': ['굴륨', '불륨', '폴륨'],
            '밝기': ['발기', '박기', '발키'],
            '단계': ['단로', '단게', '단꼐'],
            '감도': ['간도', '각도', '갑도'],
            '민감도': ['민간도', '민갑도', '민깜도'],
            '조정': ['조점', '조성', '쪼정'],
            '설정': ['설점', '설성', '셀정'],
            '실행': ['실헹', '설행', '실행'],
            '가동': ['가등', '가똥', '까동'],
            '위치': ['위기', '우치', '위지'],
            '돌아가': ['돌아까', '도라가', '돌아까'],
            '확인': ['확인', '확림', '활인'],
            '연동': ['련동', '엽동', '연똥'],
            '내일': ['래일', '네일', '낼'],
            '여기': ['여기', '여지', '역기'],
            '오늘': ['오늚', '오늘', '오늦'],
            '공간': ['공깐', '곡간', '공칸'],
            '기능': ['키능', '기응', '긴능'],
            '중단': ['중딴', '충단', '중탄'],
            '금지': ['금기', '금치', '근지'],
            '모드': ['모도', '모들', '묘드'],
            '충전': ['충정', '충젼', '춘전'],
            '센서': ['센셔', '샌서', '센소'],
            '유기': ['우기', '육기', '유끼'],
            '화합물': ['화합불', '화합몰', '활합물'],
            '화씨': ['화시', '화세', '확씨'],
            '온도': ['온또', '온토', '운도'],
            '단위': ['단의', '단이', '탄위'],
            '언어': ['어어', '언에', '연어'],
            '종류': ['종리', '종뉴', '종유'],
            '풍량': ['풍양', '퐁량', '풍냥'],
            '강풍': ['강퐁', '깡풍', '강풍'],
            '약하게': ['야카게', '약카게', '야하게'],
            '조절': ['조절', '조잘', '쪼절'],
            '스캐닝': ['스케닝', '스캔닝', '스캐링'],
            '종료': ['종뇨', '종료', '종료'],
            '표시': ['표기', '표시', '표지'],
            '전망': ['전방', '전망', '저망'],
            '상태': ['상대', '상태', '상테'],
            '결과': ['걸과', '결과', '걸화'],
            '보고서': ['보고셔', '보고세', '복서'],
            '화면': ['화멘', '화먼', '활면'],
            '설명': ['설멍', '설명', '셜명'],
            '주의': ['주이', '주의', '쥬의'],
            '사항': ['사향', '사항', '사앙'],
            '어린이': ['어리이', '얼이', '어린'],
            '유아': ['유어', '육아', '유악'],
            '부실': ['부싫', '부식', '부신'],
            '동작': ['동잘', '돈작', '동짜'],
            '시작': ['시잘', '시착', '지작'],
            '방해': ['방헤', '방애', '방혜']
        }

        self.spacing_errors = [
            ('알려 줘', '알려줘'),
            ('보여 줘', '보여줘'),
            ('해 줘', '해줘'),
            ('맞춰 줘', '맞춰줘'),
            ('설정해 줘', '설정해줘'),
            ('조정해 줘', '조정해줘'),
            ('가동해 줘', '가동해줘'),
            ('실행해 줘', '실행해줘'),
            ('확인해 줘', '확인해줘'),
            ('공기 청정', '공기청정'),
            ('대기 질', '대기질'),
            ('모니터 링', '모니터링'),
            ('에이 아이', '에이아이'),
            ('AI 모드', 'AI모드'),
            ('음성 인식', '음성인식'),
            ('방해 금지', '방해금지'),
            ('충전 위치', '충전위치'),
            ('고정 청정', '고정청정'),
            ('전체 공간', '전체공간'),
            ('감지 감도', '감지감도'),
            ('센서 감도', '센서감도'),
            ('민감 도', '민감도'),
            ('소리 볼륨', '소리볼륨'),
            ('화면 밝기', '화면밝기'),
            ('LED 밝기', 'LED밝기'),
            ('온도 단위', '온도단위'),
            ('언어 설정', '언어설정'),
            ('음성 설정', '음성설정'),
            ('바람 세기', '바람세기'),
            ('풍량 조절', '풍량조절'),
            ('스캐닝 모드', '스캐닝모드'),
            ('청정 모드', '청정모드'),
            ('웰컴 기능', '웰컴기능'),
            ('실외 대기질', '실외대기질'),
            ('공기질 연동', '공기질연동'),
            ('정보 연동', '정보연동'),
            ('그 다음에', '그다음에'),
            ('그 후에', '그후에'),
            ('그리고 나서', '그리고나서'),
            ('이어 서', '이어서'),
            ('또한 ', '또'),
            ('다음 으로', '다음으로'),
            (' 의 ', '의'),
            (' 에 ', '에'),
            (' 를 ', '를'),
            (' 로 ', '로')
        ]

        self.endings = {
            '어때': ['없대', '어떄', '어대요'],
            '할까': ['할가', '할까요', '할께'],
            '있어': ['이써', '있죠', '있어요'],
            '줘': ['져', '주세요', '줄래'],
            '해': ['헤', '하세요', '할래'],
            '가': ['까', '가요', '갈래'],
            '나': ['냐', '나요', '날래']
        }

        # 확률적 적용을 위한 확률값 설정
        self.word_error_prob = 0.3
        self.spacing_error_prob = 1.0
        self.dup_error_prob = 0.0
        self.ending_error_prob = 1.0

        # 여러 오류 동시 적용을 위한 확률 설정
        self.multi_error_prob = 0.1  # 여러 오류를 동시에 적용할 확률
        self.max_simultaneous_errors = 2  # 동시에 적용할 수 있는 최대 오류 수

    def get_applicable_phonetic_errors(self, text: str) -> Dict[str, List[str]]:
        """텍스트에 적용 가능한 발음 오류 패턴 반환"""
        applicable = {}
        for correct, errors in self.phonetic_errors.items():
            if correct in text:
                applicable[correct] = errors
        return applicable

    def get_applicable_word_errors(self, text: str) -> Dict[str, List[str]]:
        """텍스트에 적용 가능한 단어 오류 패턴 반환"""
        applicable = {}
        for correct, errors in self.word_errors.items():
            if correct in text:
                applicable[correct] = errors
        return applicable

    def get_applicable_spacing_errors(self, text: str) -> List[tuple]:
        """텍스트에 적용 가능한 띄어쓰기 오류 패턴 반환"""
        applicable = []
        for correct, error in self.spacing_errors:
            if correct in text:
                applicable.append((correct, error))
        return applicable

    def get_applicable_word_duplications(self, text: str) -> List[int]:
        """텍스트에 적용 가능한 단어 중복 위치 반환"""
        words = text.split()
        if len(words) > 3:
            return list(range(1, len(words) - 1))
        return []

    def get_applicable_ending_variations(self, text: str) -> List[str]:
        """텍스트에 적용 가능한 어미 변화 반환"""
        for correct, variations in self.endings.items():
            if text.endswith(correct):
                return variations
        return []

    def apply_phonetic_error(self, text: str, correct: str, error: str) -> str:
        """발음 오류 적용"""
        return text.replace(correct, error)

    def apply_word_error(self, text: str, correct: str, error: str) -> str:
        """단어 오류 적용"""
        return text.replace(correct, error, 1)  # 첫 번째 발견만 교체

    def apply_spacing_error(self, text: str, correct: str, error: str) -> str:
        """띄어쓰기 오류 적용"""
        return text.replace(correct, error)

    def apply_word_duplication(self, text: str, idx: int) -> str:
        """단어 중복 적용"""
        words = text.split()
        if idx < 0 or idx >= len(words):  # 인덱스 유효성 검사 추가
            return text
        words.insert(idx, words[idx])
        return ' '.join(words)

    def apply_ending_variation(self, text: str, variation: str) -> str:
        """어미 변화 적용"""
        for correct, variations in self.endings.items():
            if text.endswith(correct) and variation in variations:
                return text[:-len(correct)] + variation
        return text

    def apply_multiple_errors(self, text: str, error_types: List[str]) -> str:
        """여러 오류를 동시에 적용"""
        current_text = text
        applied_errors = []

        for error_type in error_types:
            if error_type == 'word' and self.get_applicable_word_errors(current_text):
                word_errors = self.get_applicable_word_errors(current_text)
                correct = random.choice(list(word_errors.keys()))
                if correct in current_text:
                    error = random.choice(word_errors[correct])
                    current_text = self.apply_word_error(current_text, correct, error)
                    applied_errors.append(f'word:{correct}->{error}')

            elif error_type == 'spacing' and self.get_applicable_spacing_errors(current_text):
                spacing_errors = self.get_applicable_spacing_errors(current_text)
                correct, error = random.choice(spacing_errors)
                current_text = self.apply_spacing_error(current_text, correct, error)
                applied_errors.append(f'spacing:{correct}->{error}')

            elif error_type == 'duplication' and self.get_applicable_word_duplications(current_text):
                word_duplications = self.get_applicable_word_duplications(current_text)
                idx = random.choice(word_duplications)
                words = current_text.split()
                duplicated_word = words[idx]
                current_text = self.apply_word_duplication(current_text, idx)
                applied_errors.append(f'duplication:{duplicated_word}')

            elif error_type == 'ending' and self.get_applicable_ending_variations(current_text):
                ending_variations = self.get_applicable_ending_variations(current_text)
                variation = random.choice(ending_variations)
                original_text = current_text
                current_text = self.apply_ending_variation(current_text, variation)
                if current_text != original_text:
                    applied_errors.append(f'ending:->{variation}')

        return current_text

    def generate_all_augmentations(self, text: str) -> List[str]:
        """텍스트의 증강 조합 생성 - phonetic_errors는 모든 경우의 수, 나머지는 확률적 적용 + 여러 오류 동시 적용"""
        augmentations = set()

        # 적용 가능한 오류 패턴들 수집
        phonetic_errors = self.get_applicable_phonetic_errors(text)
        word_errors = self.get_applicable_word_errors(text)
        spacing_errors = self.get_applicable_spacing_errors(text)
        word_duplications = self.get_applicable_word_duplications(text)
        ending_variations = self.get_applicable_ending_variations(text)

        # 1. phonetic_errors - 모든 경우의 수 적용
        phonetic_variations = [text]  # 원본부터 시작

        for correct, errors in phonetic_errors.items():
            new_variations = []
            for base_text in phonetic_variations:
                new_variations.append(base_text)  # 원본 유지
                for error in errors:
                    if correct in base_text:
                        augmented = self.apply_phonetic_error(base_text, correct, error)
                        new_variations.append(augmented)
            phonetic_variations = new_variations

        # phonetic_errors 적용된 모든 변형을 기본으로 사용
        for base_text in phonetic_variations:
            # 2. 기존 방식: 단일 오류 확률적 적용
            current_text = base_text

            # word_errors - 확률적 적용
            if word_errors and random.random() < self.word_error_prob:
                correct = random.choice(list(word_errors.keys()))
                if correct in current_text:
                    error = random.choice(word_errors[correct])
                    current_text = self.apply_word_error(current_text, correct, error)

            # spacing_errors - 확률적 적용
            applicable_spacing = self.get_applicable_spacing_errors(current_text)
            if applicable_spacing and random.random() < self.spacing_error_prob:
                correct, error = random.choice(applicable_spacing)
                current_text = self.apply_spacing_error(current_text, correct, error)

            # word_duplications - 낮은 확률로 적용
            if word_duplications and random.random() < self.dup_error_prob:
                idx = random.choice(word_duplications)
                current_text = self.apply_word_duplication(current_text, idx)

            # ending_variations - 낮은 확률로 적용
            if ending_variations and random.random() < self.ending_error_prob:
                variation = random.choice(ending_variations)
                current_text = self.apply_ending_variation(current_text, variation)

            augmentations.add(current_text)

            # 3. 새로운 방식: 여러 오류 동시 적용
            if random.random() < self.multi_error_prob:
                multi_error_variants = self.generate_multi_error_combinations(base_text)
                for variant in multi_error_variants:
                    augmentations.add(variant)

        # 원본 제거하고 유니크한 증강 데이터만 반환
        augmentations.discard(text)
        return list(augmentations)

    def generate_multi_error_combinations(self, text: str) -> List[str]:
        """여러 오류의 조합을 생성"""
        augmentations = set()

        # 적용 가능한 오류 타입들 확인
        available_error_types = []
        if self.get_applicable_word_errors(text):
            available_error_types.append('word')
        if self.get_applicable_spacing_errors(text):
            available_error_types.append('spacing')
        if self.get_applicable_word_duplications(text):
            available_error_types.append('duplication')
        if self.get_applicable_ending_variations(text):
            available_error_types.append('ending')

        if not available_error_types:
            return []

        # 다양한 조합 생성 (2개부터 최대 개수까지)
        for combo_size in range(2, min(len(available_error_types) + 1, self.max_simultaneous_errors + 1)):
            for error_combo in combinations(available_error_types, combo_size):
                # 각 조합을 여러 번 시도하여 다양한 변형 생성
                for _ in range(3):  # 각 조합당 3번 시도
                    augmented = self.apply_multiple_errors(text, list(error_combo))
                    if augmented != text:
                        augmentations.add(augmented)

        return list(augmentations)

    def augment_dataset(self, train_data_path: str, output_path: str, include_original: bool = True):
        """훈련 데이터셋을 모든 가능한 경우의 수로 증강하여 새로운 파일로 저장

        Args:
            train_data_path: 원본 훈련 데이터 파일 경로
            output_path: 출력 파일 경로
            include_original: 원본 데이터를 결과에 포함할지 여부 (기본값: True)
        """
        # 원본 데이터 로드
        df = pd.read_csv(train_data_path)
        print(f"원본 데이터 크기: {len(df)}")

        # 증강된 데이터를 저장할 리스트
        augmented_data = []

        # 원본 데이터 추가 (선택적)
        if include_original:
            for _, row in df.iterrows():
                augmented_data.append({
                    'Index': row['Index'],
                    'Query(한글)': row['Query(한글)'],
                    'LLM Output': row['LLM Output'],
                })
            print("원본 데이터가 결과에 포함됩니다.")
        else:
            print("원본 데이터는 결과에 포함되지 않습니다.")

        # 데이터 증강 - 모든 가능한 조합
        augmentation_count = 0
        for idx, row in df.iterrows():
            original_query = row['Query(한글)']
            augmented_queries = self.generate_all_augmentations(original_query)

            for aug_idx, augmented_query in enumerate(augmented_queries):
                augmented_data.append({
                    'Index': f"{row['Index']}",
                    'Query(한글)': augmented_query,
                    'LLM Output': row['LLM Output'],
                })
                augmentation_count += 1

        # 결과를 DataFrame으로 변환
        result_df = pd.DataFrame(augmented_data)

        original_count = len(df) if include_original else 0
        print(f"최종 데이터 크기: {len(result_df)} (원본: {original_count}, 증강: {augmentation_count})")

        # CSV 파일로 저장
        result_df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"증강된 데이터가 {output_path}에 저장되었습니다.")

        return result_df


if __name__ == "__main__":
    # 데이터 증강 실행
    augmenter = STTDataAugmenter()

    train_data_path = "train_data_origin.csv"
    output_path = "train_data_stt.csv"

    print("=== STT 증강 ===")
    augmented_df = augmenter.augment_dataset(train_data_path, output_path, include_original=True)
