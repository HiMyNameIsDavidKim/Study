import pandas as pd
import re
import random


class DayDataAugmenter:
    def __init__(self, seed=None, prob=0.3):
        # 요일 및 특수 timeframe 매핑
        self.timeframe_to_day = {
            0: "오늘",
            1: "내일",
            2: "주말",
            3: "월요일",
            4: "화요일",
            5: "수요일",
            6: "목요일",
            7: "금요일",
            8: "토요일",
            9: "일요일"
        }
        self.func_pattern = re.compile(r'<function_(MO|IO)\>\(timeframe=(\d+), location=([^\)]+)\)')
        self.kor_day_pattern = re.compile(r'(오늘|현재|지금|내일|주말|월요일|화요일|수요일|목요일|금요일|토요일|일요일)')
        self.prob = prob
        if seed is not None:
            random.seed(seed)

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
            for match in self.func_pattern.finditer(llm_output):
                func, old_timeframe, location = match.groups()
                old_timeframe = int(old_timeframe)
                # 30% 확률로만 증강
                if random.random() < self.prob:
                    for tf, day_kor in self.timeframe_to_day.items():
                        new_llm_output = llm_output[:match.start()] + \
                            f'<function_{func}>(timeframe={tf}, location={location})' + \
                            llm_output[match.end():]
                        if self.kor_day_pattern.search(query):
                            if tf == 0:
                                new_query = self.kor_day_pattern.sub("오늘", query)
                            else:
                                new_query = self.kor_day_pattern.sub(day_kor, query)
                        else:
                            new_query = query
                        new_row = row.copy()
                        new_row['Query(한글)'] = new_query
                        new_row['LLM Output'] = new_llm_output
                        aug_rows.append(new_row)
                        aug_count += 1
                        found = True
                else:
                    if include_original:
                        aug_rows.append(row)
                    found = True
            if not found and include_original:
                aug_rows.append(row)
        aug_df = pd.DataFrame(aug_rows)
        print(f"최종 데이터 크기: {len(aug_df)} (원본: {len(df)}, 증강: {aug_count})")
        if output_path:
            aug_df.to_csv(output_path, index=False)
            print(f"증강된 데이터가 {output_path}에 저장되었습니다.")
        return aug_df

if __name__ == "__main__":
    # 데이터 증강 실행 예시
    augmenter = DayDataAugmenter()

    train_data_path = "train_data_origin.csv"
    output_path = "train_data_days.csv"

    print("=== Day 증강 ===")
    augmented_df = augmenter.augment_dataset(train_data_path, output_path, include_original=True)
    print(augmented_df.head(10))
