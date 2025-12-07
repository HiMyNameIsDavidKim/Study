#!/usr/bin/env python3
"""
PEFT 어댑터를 베이스 모델에 병합하여 vLLM 호환 모델 생성
"""

import logging
import os

import torch
from peft import PeftModel
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def merge_peft_model(base_model_name: str, peft_model_path: str, output_path: str, device_map: str = "auto"):
    """
    PEFT 어댑터를 베이스 모델에 병합합니다.

    Args:
        base_model_name: 베이스 모델명
        peft_model_path: PEFT 어댑터 경로
        output_path: 병합된 모델 저장 경로
        device_map: 디바이스 맵
    """
    logger.info(f"베이스 모델 로드: {base_model_name}")

    # 베이스 모델 로드
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name, torch_dtype=torch.float16, device_map=device_map, trust_remote_code=True
    )

    logger.info(f"PEFT 어댑터 로드: {peft_model_path}")

    # PEFT 모델 로드
    model = PeftModel.from_pretrained(base_model, peft_model_path)

    logger.info("어댑터를 베이스 모델에 병합 중...")

    # 어댑터 병합
    merged_model = model.merge_and_unload()

    logger.info("토크나이저 및 설정 로드...")

    # 토크나이저와 설정 로드
    tokenizer = AutoTokenizer.from_pretrained(peft_model_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    config = AutoConfig.from_pretrained(base_model_name, trust_remote_code=True)

    logger.info(f"병합된 모델 저장: {output_path}")

    # 저장
    os.makedirs(output_path, exist_ok=True)
    merged_model.save_pretrained(output_path, safe_serialization=True)
    tokenizer.save_pretrained(output_path)
    config.save_pretrained(output_path)

    logger.info("모델 병합 완료!")

    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(description="PEFT 모델 병합")
    parser.add_argument("--base_model", type=str, default="meta-llama/Llama-3.2-1B-Instruct", help="베이스 모델명")
    parser.add_argument("--peft_model", type=str, default="./my_finetuned_model_v2", help="PEFT 모델 경로")
    parser.add_argument("--output", type=str, default="./llama_function_call_merged", help="출력 경로")

    args = parser.parse_args()

    merge_peft_model(args.base_model, args.peft_model, args.output)


if __name__ == "__main__":
    main()
