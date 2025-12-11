import pandas as pd
import re

class OrderDataAugmenter:
    def __init__(self, prob=1.0, seed=None):
        self.prob = prob
        if seed is not None:
            import random
            random.seed(seed)
        # 여러 split_token 지원
        self.split_tokens = ['그 다음에', '그리고', '또', '그 후에', '그러고 나서']
        self.func_call_pattern = re.compile(r'<function_[^>]+>\([^)]*\)')

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
            # 여러 split_token 중 가장 먼저 등장하는 것으로 split
            token_found = None
            token_pos = len(query) + 1
            for token in self.split_tokens:
                pos = query.find(token)
                if pos != -1 and pos < token_pos:
                    token_found = token
                    token_pos = pos
            if token_found:
                parts = query.split(token_found)
                if len(parts) == 2:
                    first, second = parts[0].strip(), parts[1].strip()
                    new_query = f"{second} {token_found} {first}"
                    # LLM Output 펑션콜 뒤집기
                    func_calls = [s.strip() for s in llm_output.split(';') if s.strip()]
                    if len(func_calls) > 1:
                        new_llm_output = '; '.join(func_calls[::-1])
                        new_row = row.copy()
                        new_row['Query(한글)'] = new_query
                        new_row['LLM Output'] = new_llm_output
                        aug_rows.append(new_row)
                        aug_count += 1
            if include_original:
                aug_rows.append(row)
        aug_df = pd.DataFrame(aug_rows)
        print(f"최종 데이터 크기: {len(aug_df)} (원본: {len(df)}, 증강: {aug_count})")
        if output_path:
            aug_df.to_csv(output_path, index=False)
            print(f"증강된 데이터가 {output_path}에 저장되었습니다.")
        return aug_df

if __name__ == "__main__":
    augmenter = OrderDataAugmenter()
    train_data_path = "train_data_origin.csv"
    output_path = "train_data_order.csv"
    print("=== Order 증강 ===")
    augmented_df = augmenter.augment_dataset(train_data_path, output_path, include_original=True)
    print(augmented_df.head(10))
