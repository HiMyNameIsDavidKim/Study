import pandas as pd
import re
import random

class SenDataAugmenter:
    def __init__(self):
        self.type_to_kor = {
            -1: "조절",
            0: "낮게",
            1: "보통으로",
            2: "높게"
        }
        self.state_words = ["민감", "보통", "낮게", "높게", "빈칸"]
        self.state_to_type = {
            "민감": 2,
            "높게": 2,
            "보통": 1,
            "보통으로": 1,
            "낮게": 0,
            "낮음": 0,
            "빈칸": -1
        }
        # type별 tail 후보군
        self.type_tail_candidates = {
            -1: ["조절해줄래", "조정해줘", "조절해줘", "조정해줄래", "설정해줘", "맞춰줘", "바꿔줘", "해줘"],
            0: ["낮음으로 바꿔줄래", "낮음으로 맞춰줘", "낮게 설정해줘", "낮게 조정해줘", "낮게 바꿔줘", "낮게 해줘"],
            1: ["보통으로 바꿔줄래", "보통으로 맞춰줘", "보통으로 설정해줘", "보통으로 조정해줘", "보통으로 바꿔줘", "보통으로 해줘"],
            2: ["높음으로 바꿔줄래", "높음으로 맞춰줘", "높게 설정해줘", "높게 조정해줘", "높게 바꿔줘", "높게 해줘"]
        }
        self.get_tail_candidates = ["상태 알려줘", "상태 확인해줘", "상태 보여줘", "상태 좀 알려줄래", "상태 좀 확인해줘"]
        # QD 함수 패턴: <function_QD>(type=2), <function_QD> ( type=2 ) 등 공백 포함 모두 매칭
        self.qd_pattern = re.compile(r'<function_QD>\s*\([^)]*\)')
        # 키워드 패턴
        self.keyword_pattern = r'(감지 감도|센서 감도|감도)'
        # 상태 단어 패턴
        self.state_pattern = r'(민감|보통|보통으로|낮게|낮음|높게|빈칸)'
        # tail 패턴
        self.tail_pattern = r'(조절해줄래|바꿔줄래|맞출래|설정해줘|해줘|조정해줘)?'
        # 전체 패턴: 키워드 + (상태) + (tail)
        self.full_pattern = re.compile(rf'{self.keyword_pattern}(?:[ ]?{self.state_pattern})?[ ]?{self.tail_pattern}')
        # tail 후보
        self.tail_candidates = ["조절해줄래", "낮음으로 바꿔줄래", "보통으로 바꿔줄래", "높음으로 바꿔줄래", "맞출래", "바꿔줄래", "조정해줘", "해줘", "조정해"]

    def replace_sen_phrase(self, query, t=None, is_get=False):
        # 조사까지 포함한 패턴: 예) 센서 감도를 민감으로 바꿔줄래, 센서 감도 조절해줄래 등
        # tail 앞에 '으로' 등 어미까지 포함
        particle = r'(?:[를은는이가도에로와과의에서에게한테까지부터밖에마저조차처럼만큼]?)'
        ending = r'(?:으로|로|게|에)?'
        # 전체 패턴: 키워드 + 조사 + (상태) + (어미) + tail
        full_pattern_with_particle = re.compile(rf'({self.keyword_pattern}){particle}(?:[ ]?{self.state_pattern})?{ending}[ ]?{self.tail_pattern}')
        # 연결어 패턴 정의
        connector_pattern = r'(그러고 나서|그리고|그 다음에|그런 다음에|이어서|그 후에)'
        # 문장을 연결어 기준으로 분리
        parts = re.split(connector_pattern, query)
        processed_parts = []
        for i, part in enumerate(parts):
            # 연결어는 그대로 추가
            if re.fullmatch(connector_pattern, part.strip()):
                processed_parts.append(part)
                continue
            # tail 후보가 있는지 먼저 탐색
            has_tail = any(tail in part for tail in self.tail_candidates)
            if not has_tail:
                continue  # tail 없는 파트는 무시
            # 기존 로직 적용
            new_query = part
            # tail이 여러 번 반복되는 경우 한 번만 남기기 및 불필요한 조사/상태/숫자/어구 제거 반복
            prev_query = None
            while prev_query != new_query:
                prev_query = new_query
                for tail in self.tail_candidates:
                    # tail 앞에 남은 숫자/상태/불필요한 단어 제거
                    new_query = re.sub(rf'([0-9]+|[민감|보통|낮게|낮음|높게|높음|상태|으로|로|게|에|\s]+)?{tail}', tail, new_query)
                    new_query = re.sub(rf'(를|은|는|이|가|도|에|로|와|과|의|에서|에게|한테|까지|부터|밖에|마저|조차|처럼|만큼)?([0-9]+|[민감|보통|낮게|낮음|높게|높음|상태|으로|로|게|에|\s]+)?{tail}', tail, new_query)
                    # tail이 여러 번 반복되는 경우 한 번만 남기기
                    new_query = re.sub(rf'(으로 )?({tail})+', tail, new_query)
                    new_query = re.sub(rf'({tail})+([., ])', rf'\1\2', new_query)
            # tail만 남기고 나머지 제거
            for tail in self.tail_candidates:
                if tail in new_query:
                    new_query = tail
                    break
            processed_parts.append(new_query)
        # 분리된 부분을 다시 연결
        return ' '.join(processed_parts).replace('  ', ' ').strip()

    def augment_dataset(self, input_path, output_path=None, include_original=True):
        df = pd.read_csv(input_path)
        print(f"원본 데이터 크기: {len(df)}")
        if include_original:
            print("원본 데이터가 결과에 포함됩니다.")
        else:
            print("원본 데이터는 결과에 포함되지 않습니다.")
        aug_rows = []
        aug_count = 0
        qd_rows = []  # QD 관련 증강 행만 따로 저장
        for idx, row in df.iterrows():
            query = str(row['Query(한글)'])
            llm_output = str(row['LLM Output'])
            found = False
            for match in self.qd_pattern.finditer(llm_output):
                found = True
                for t in [-1, 0, 1, 2]:
                    new_row = row.copy()
                    new_row['Query(한글)'] = self.replace_sen_phrase(query, t=t, is_get=False)
                    new_llm_output = self.qd_pattern.sub(f'<function_QD>(type={t})', llm_output)
                    new_row['LLM Output'] = new_llm_output
                    aug_rows.append(new_row)
                    qd_rows.append(new_row)
                    aug_count += 1
                # get=True 증강
                new_row = row.copy()
                new_row['Query(한글)'] = self.replace_sen_phrase(query, is_get=True)
                new_llm_output = self.qd_pattern.sub('<function_QD>(get=True)', llm_output)
                new_row['LLM Output'] = new_llm_output
                aug_rows.append(new_row)
                qd_rows.append(new_row)
                aug_count += 1
            if not found and include_original:
                aug_rows.append(row)
        aug_df = pd.DataFrame(aug_rows)
        if output_path:
            aug_df.to_csv(output_path, index=False)
        # # QD 관련 증강 행만 별도 저장
        # if len(qd_rows) > 0:
        #     pd.DataFrame(qd_rows).to_csv("train_data_sen_qdonly.csv", index=False)
        print(f"최종 데이터 크기: {len(aug_df)} (원본: {len(df)}, 증강: {aug_count})")
        if output_path:
            aug_df.to_csv(output_path, index=False)
            print(f"증강된 데이터가 {output_path}에 저장되었습니다.")
        return aug_df

if __name__ == "__main__":
    augmenter = SenDataAugmenter()
    train_data_path = "train_data_origin.csv"
    output_path = "train_data_sen.csv"
    print("=== Sen 증강 ===")
    augmented_df = augmenter.augment_dataset(train_data_path, output_path, include_original=True)
