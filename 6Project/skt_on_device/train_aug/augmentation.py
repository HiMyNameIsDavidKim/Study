from stt_aug import STTDataAugmenter
from days_aug import DayDataAugmenter
from order_aug import OrderDataAugmenter
from sen_aug import SenDataAugmenter
from bri_aug import BriDataAugmenter


if __name__ == "__main__":
    # 데이터 증강 실행
    stt_augmenter = STTDataAugmenter()
    day_augmenter = DayDataAugmenter()
    order_augmenter = OrderDataAugmenter()
    sen_augmenter = SenDataAugmenter()
    bri_augmenter = BriDataAugmenter()

    train_data_path = "train_data_origin.csv"
    output_path = "train_data.csv"

    print("=== STT 증강 ===")
    augmented_df = stt_augmenter.augment_dataset(train_data_path, output_path, include_original=True)

    print("=== Day 증강 ===")
    augmented_df = day_augmenter.augment_dataset(output_path, output_path, include_original=True)

    print("=== Order 증강 ===")
    augmented_df = order_augmenter.augment_dataset(output_path, output_path, include_original=True)

    print("=== Sen 증강 ===")
    augmented_df = sen_augmenter.augment_dataset(output_path, output_path, include_original=True)

    print("=== Bri 증강 ===")
    augmented_df = bri_augmenter.augment_dataset(output_path, output_path, include_original=True)
