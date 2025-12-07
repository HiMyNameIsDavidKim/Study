import pandas as pd
import re
import random

class BriDataAugmenter:
    def __init__(self):
        # brightness 값별 자연스러운 표현 후보군
        self.brightness_to_kor = {
            -1: ["조절", "조정", "맞춰", "설정"],
            0: ["꺼줘", "0프로로 바꿔", "0으로 바꿔", "0단계로 바꿔", "0%로 바꿔", "0단계로 설정해줘"],
            1: ["이십프로로 바꿔", "1로 바꿔", "1단계로 바꿔", "20%로 바꿔", "20프로로 바꿔", "1단계로 설정해줘"],
            2: ["사십프로로 바꿔", "2로 바꿔", "2단계로 바꿔", "40%로 바꿔", "40프로로 바꿔", "2단계로 설정해줘"],
            3: ["육십프로로 바꿔", "3로 바꿔", "3단계로 바꿔", "60%로 바꿔", "60프로로 바꿔", "3단계로 설정해줘"],
            4: ["팔십프로로 바꿔", "4로 바꿔", "4단계로 바꿔", "80%로 바꿔", "80프로로 바꿔", "4단계로 설정해줘"],
            5: ["백프로로 바꿔", "5로 바꿔", "5단계로 바꿔", "100%로 바꿔", "100프로로 바꿔", "5단계로 설정해줘"]
        }
        # tail 후보군에서 비문(몇야 등) 제거, 자연스러운 tail만 사용
        self.get_tail_candidates = [
            "몇프로인지 알려줘", "밝기 상태 알려줘", "밝기 몇프로야", "밝기 상태 확인해줘", "밝기 보여줘", "밝기 좀 알려줄래"
        ]
        # function_WN 패턴: <function_WN>(brightness=2), <function_WN> ( brightness=2 ) 등
        self.wn_pattern = re.compile(r'<function_WN>\s*\([^)]*\)')
        # 밝기 관련 키워드 패턴 (확장)
        self.keyword_pattern = r'(밝기|화면 밝기|엘이디|엘씨디|조도|LED 밝기|LCD 밝기|LED|LCD|화면)'
        # tail 후보
        self.tail_candidates = [
            "조절해줘", "조정해줘", "설정해줘", "바꿔줘", "맞춰줘", "해줘"
        ]

    def clean_phrase(self, phrase):
        # tail 중복 및 불필요한 단어/조사/공백/반복 제거 (kor는 남기고 tail만 정제)
        for tail in set(self.tail_candidates):
            phrase = re.sub(rf'({tail})+', tail, phrase)
        # tail이 여러 번 반복되는 경우 한 번만 남기기
        phrase = re.sub(r'(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)(\s*\1)+', r'\1', phrase)
        # '조정 조정해줘'처럼 단어와 단어+해줘의 반복 제거
        phrase = re.sub(r'(조정|조절|설정|맞춰|바꿔|줄여|켜|꺼)[ ]*(조정해줘|조절해줘|설정해줘|맞춰줘|바꿔줘|줄여줘|켜줘|꺼줘)', r'\2', phrase)
        # '조정 조정해줘' 등 중복 단어 제거
        phrase = re.sub(r'(조정|조절|설정|맞춰|바꿔|줄여|켜|꺼)\s*\1+', r'\1', phrase)
        # '밝기 밝기', '조명 조명' 등 키워드 중복 제거
        phrase = re.sub(r'(밝기|조명|엘이디|엘씨디|LCD|LED) \1', r'\1', phrase)
        # tail 앞에 붙는 불필요한 tail만 제거 (kor는 남김)
        phrase = re.sub(r'(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)[ ]*(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)+', r'\1', phrase)
        # tail 뒤에 붙는 불필요한 단어/공백/숫자/한글/특수문자 제거
        phrase = re.sub(r'(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)[^\w\s]+', r'\1', phrase)
        # tail 뒤에 붙은 모든 문자 제거(최종)
        phrase = re.sub(r'(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)[가-힣0-9%a-zA-Z!@#$%^&*()_+=\-\[\]{}|;:",.<>/?`~]*$', r'\1', phrase)
        # 불필요한 공백 정리
        phrase = re.sub(r'\s+', ' ', phrase).strip()
        return phrase

    def replace_bri_phrase(self, query, brightness=None, is_get=False):
        get_tail_candidates = [
            "몇프로인지 알려줘", "밝기 상태 알려줘", "밝기 몇프로야", "밝기 상태 확인해줘", "밝기 보여줘", "밝기 좀 알려줄래"
        ]
        parts = [p.strip() for p in query.split(';')]
        new_parts = []
        wn_found = False
        for part in parts:
            if re.search(self.keyword_pattern, part) or re.search(self.wn_pattern, part):
                wn_found = True
                if is_get:
                    tail = random.choice(get_tail_candidates)
                    m = re.search(self.keyword_pattern, part)
                    if m:
                        prefix = part[:m.end()]
                        # 기존 키워드 뒤의 tail/수치/단계/프로/퍼센트 등 모두 제거
                        suffix = re.sub(r'([를은는이가]?)[ ]*(\d+|[영일이삼사오육칠팔구십백천]+)?(단계|프로|%|퍼센트)?(로|으로)?[ ]*(밝기|조명|퍼|프로|단계|%|조정|조절|설정|맞춰|바꿔|줄여|켜|꺼)?[ ]*(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)?[가-힣0-9%a-zA-Z!@#$%^&*()_+=\-\[\]{}|;:",.<>/?`~]*$', '', part[m.end():])
                        phrase = prefix + ' ' + tail
                    else:
                        phrase = f"밝기 {tail}"
                    phrase = self.clean_phrase(phrase)
                    new_parts.append(phrase)
                elif brightness is not None:
                    kor_candidates = self.brightness_to_kor.get(brightness, ["조절"])
                    kor = random.choice(kor_candidates)
                    tail = random.choice(self.tail_candidates)
                    m = re.search(self.keyword_pattern, part)
                    if m:
                        prefix = part[:m.end()]
                        # 기존 키워드 뒤의 tail/수치/단계/프로/퍼센트 등 모두 제거
                        suffix = re.sub(r'([를은는이가]?)[ ]*(\d+|[영일이삼사오육칠팔구십백천]+)?(단계|프로|%|퍼센트)?(로|으로)?[ ]*(밝기|조명|퍼|프로|단계|%|조정|조절|설정|맞춰|바꿔|줄여|켜|꺼)?[ ]*(해줘|조정해줘|설정해줘|바꿔줘|맞춰줘|조절해줘)?[가-힣0-9%a-zA-Z!@#$%^&*()_+=\-\[\]{}|;:",.<>/?`~]*$', '', part[m.end():])
                        phrase = prefix + ' ' + kor + ' ' + tail
                    else:
                        phrase = f"밝기 {kor} {tail}"
                    phrase = self.clean_phrase(phrase)
                    new_parts.append(phrase)
                else:
                    new_parts.append(self.clean_phrase(part))
            else:
                new_parts.append(part)
        if not wn_found:
            return self.clean_phrase(query)
        return '; '.join([p for p in new_parts if p]).strip()

    def augment_dataset(self, input_path, output_path=None, include_original=True):
        df = pd.read_csv(input_path)
        print(f"원본 데이터 크기: {len(df)}")
        if include_original:
            print("원본 데이터가 결과에 포함됩니다.")
        else:
            print("원본 데이터는 결과에 포함되지 않습니다.")
        aug_rows = []
        aug_count = 0
        for idx, row in df.iterrows():
            query = str(row['Query(한글)'])
            llm_output = str(row['LLM Output'])
            found = False
            for match in self.wn_pattern.finditer(llm_output):
                found = True
                for b in [-1, 0, 1, 2, 3, 4, 5]:
                    new_row = row.copy()
                    new_row['Query(한글)'] = self.replace_bri_phrase(query, brightness=b, is_get=False)
                    new_llm_output = self.wn_pattern.sub(f'<function_WN>(brightness={b})', llm_output)
                    new_row['LLM Output'] = new_llm_output
                    aug_rows.append(new_row)
                    aug_count += 1
                # get=True 증강
                new_row = row.copy()
                new_row['Query(한글)'] = self.replace_bri_phrase(query, is_get=True)
                new_llm_output = self.wn_pattern.sub('<function_WN>(get=True)', llm_output)
                new_row['LLM Output'] = new_llm_output
                aug_rows.append(new_row)
                aug_count += 1
            if not found and include_original:
                aug_rows.append(row)
        aug_df = pd.DataFrame(aug_rows)
        if output_path:
            aug_df.to_csv(output_path, index=False)
        print(f"최종 데이터 크기: {len(aug_df)} (원본: {len(df)}, 증강: {aug_count})")
        if output_path:
            print(f"증강된 데이터가 {output_path}에 저장되었습니다.")
        return aug_df

if __name__ == "__main__":
    augmenter = BriDataAugmenter()
    train_data_path = "train_data_origin.csv"
    output_path = "train_data_bri.csv"
    print("=== Bri 증강 ===")
    augmented_df = augmenter.augment_dataset(train_data_path, output_path, include_original=True)
