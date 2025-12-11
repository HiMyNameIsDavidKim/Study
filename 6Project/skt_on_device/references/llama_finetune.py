import logging
import os
from typing import Any, Dict, List

import pandas as pd
import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

# 로깅
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LlamaFunctionCallTrainer:
    def __init__(self, model_name: str = "meta-llama/Llama-3.2-1B-Instruct"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.quantization_config = None
        self.compute_dtype = torch.float16

    def _pick_compute_dtype(self, prefer_bf16=True):
        if prefer_bf16 and torch.cuda.is_available():
            try:
                if torch.cuda.is_bf16_supported():
                    return torch.bfloat16
            except Exception:
                pass
        return torch.float16

    def load_model_and_tokenizer(self, load_in_4bit=True):
        logger.info(f"Loading model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.compute_dtype = self._pick_compute_dtype()
        self.quantization_config = BitsAndBytesConfig(
            load_in_4bit=load_in_4bit,
            bnb_4bit_compute_dtype=self.compute_dtype,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=self.compute_dtype,
            device_map="auto",
            trust_remote_code=True,
            quantization_config=self.quantization_config,
        )
        self.model.resize_token_embeddings(len(self.tokenizer))
        self.model.config.use_cache = False
        logger.info("Model loaded.")

    def load_function_call_data(self, data_paths: List[str]) -> pd.DataFrame:
        dfs = []
        for path in data_paths:
            if os.path.exists(path):
                df = pd.read_csv(path, encoding="utf-8", index_col=0)
                dfs.append(df)
        if not dfs:
            raise FileNotFoundError("No valid dataset found.")
        return pd.concat(dfs)

    def prepare_training_data(self, raw_data: pd.DataFrame) -> Dataset:
        formatted = []
        for idx, row in raw_data.iterrows():
            query = row.get("Query(한글)", "")
            output = row.get("LLM Output", "")
            system_prompt = """
Convert the Korean user command to `<function_identifier>()<end>` format.
(Korean user commands include typos and noise, but use correct spelling in function calls.)
# FUNCTION HINT: function_MO=날씨, function_IO=공기질, function_PG=청정 or 공청, function_QD=감지, function_BS=고스트 or 방해금지
# PARAMETER HINT: timeframe=1(내일), 2(주말), 3(월요일) ~ 9(일요일) / location=0(여기) or 지역명(띄어쓰기가 없는 표준 맞춤법 지역명)
"""
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
                {"role": "assistant", "content": output},
            ]
            if hasattr(self.tokenizer, "apply_chat_template"):
                text = self.tokenizer.apply_chat_template(messages, tokenize=False)
            else:
                text = f"{system_prompt}\n\n사용자 명령: {query}\n\n{output}"
            formatted.append({"text": text})
        return Dataset.from_list(formatted)

    def tokenize_function(self, examples):
        tokens = self.tokenizer(
            examples["text"],
            truncation=True,
            padding="max_length",
            max_length=256,
            return_tensors="pt",
        )
        tokens["labels"] = tokens["input_ids"].clone()
        return tokens

    def setup_lora_config(self) -> LoraConfig:
        return LoraConfig(
            r=32,
            lora_alpha=64,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
            lora_dropout=0.1,
            bias="none",
            task_type="CAUSAL_LM",
        )

    def fine_tune_model(self, dataset: Dataset, output_dir="./fine_tuned_model", args: Dict[str, Any] | None = None):
        logger.info("Fine-tuning start")
        args = args or {}
        lora_config = self.setup_lora_config()
        if self.quantization_config:
            self.model = prepare_model_for_kbit_training(self.model)
        self.model = get_peft_model(self.model, lora_config)

        tokenized_dataset = dataset.map(self.tokenize_function, batched=True, remove_columns=dataset.column_names)

        use_bf16 = self.compute_dtype == torch.bfloat16
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=args.get("num_train_epochs", 5),
            per_device_train_batch_size=args.get("batch_size", 8),
            # gradient_accumulation_steps=args.get("grad_accum_steps", 16),  # 실효 batch = 128
            learning_rate=args.get("learning_rate", 5e-4),
            warmup_ratio=0.05,
            lr_scheduler_type="cosine",
            fp16=not use_bf16,
            bf16=use_bf16,
            logging_steps=1,
            save_steps=10,
            save_strategy="epoch",
            report_to="none",
        )

        data_collator = DataCollatorForLanguageModeling(self.tokenizer, mlm=False)
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_dataset,
            tokenizer=self.tokenizer,
            data_collator=data_collator,
        )

        trainer.train()
        trainer.save_model()
        self.tokenizer.save_pretrained(output_dir)
        logger.info(f"Model saved to {output_dir}")


if __name__ == "__main__":
    trainer = LlamaFunctionCallTrainer("meta-llama/Llama-3.2-1B-Instruct")
    trainer.load_model_and_tokenizer(load_in_4bit=True)
    raw_data = trainer.load_function_call_data(["/mnt/elice/dataset/train_data.csv"])
    dataset = trainer.prepare_training_data(raw_data)
    trainer.fine_tune_model(dataset, output_dir="./my_finetuned_model_v2")
