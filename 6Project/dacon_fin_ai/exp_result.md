# FinAI

## License
* apache-2.0
  * skt/A.X-4.0-Light
  * kakaocorp/kanana-1.5-8b-instruct-2505
  * Qwen/Qwen3-14B
  * openai/gpt-oss-20b
  * TheFinAI/Fin-o1-8B
  * EleutherAI/polyglot-ko-5.8b
* mit
  * K-intelligence/Midm-2.0-Base-Instruct
* limited
  * LGAI-EXAONE/EXAONE-4.0-1.2B -> (OK)
  * naver-hyperclovax/HyperCLOVAX-SEED



## 성능 측정
* Qwen
  * Qwen3-1.7B_pv2: 0.4677
  * Qwen3-4B_pv2: 0.5568
  * Qwen3-4B_pv3: 0.5662
  * Qwen3-4B_pv4: 0.5873 (best)
  * Qwen3-4B_thinking_pv4: 0.5630
  * Qwen3-4B_pv5: 0.5750
  * Qwen3-4B_pv6: 0.5578
  * Qwen3-8B_pv2: 0.5533
  * Qwen3-14B_pv2: 0.5732
  * Qwen3-14B_pv4: 0.5566
  * Qwen3-14B_pv5: 0.5533
  * Qwen3-4B_rv1_01-03_pv8: 0.5582
  * Qwen3-4B_rv2_03_pv8: 0.5372
* Korean
  * A.X-4.0-Light_pv2: 0.5938 (best)
  * A.X-4.0-Light_pv4: 0.5405
  * A.X-4.0-Light_pv7: 0.5555
  * kanana-1.5-8b-instruct-2505_pv2: 0.5062
  * Midm-2.0-Base-Instruct_pv2: 0.5668
  * EXAONE-4.0-1.2B_pv4: 0.5668 (best)
  * EXAONE-4.0-1.2B_thinking_pv4: 0.5182
* oss
  * gpt-oss-20b: 0.50
* Thinking
  * 성능 안좋아짐.
  * 실행 금지.
* RAG
  * A.X-4.0-Light: 0.4704
  * EXAONE-4.0-1.2B_rv1_03-07-n04_pv8: 0.4957
  * Qwen3-4B_rv1_03-07-n04_pv8: 0.5709
  * 프롬프트
    * Qwen3-4B_rv2_03-07-n04_pv9: 0.5671
    * Qwen3-4B_rv3_03-07-n04_pv9: 0.5812
    * Qwen3-4B_rv4_03-07-n04_pv9: 0.5743
    * Qwen3-4B_rv5_03-07-n04_pv9: 0.5622
    * Qwen3-4B_rv3_03-07-n04_pv10: 0.5825
  * 하이퍼 파라미터
    * Qwen3-4B_rv3_03-07-n04_pv11: 0.5807
    * Qwen3-4B_rv6_03-14-n04_pv11 (4bit) (token base): 0.6269
    * Qwen3-4B_rv6_03-14-n04_pv11 (4bit) (token temp=0.4): 0.6390 (best)
    * Qwen3-4B_rv6_03-14-n04_pv11 (4bit) (token temp=0.1): 0.6164
    * Qwen3-4B_rv6_03-14-n04_pv11 (4bit) (gen base): 0.6058
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen base): 0.6346
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen temp=0.4): 0.6070
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen temp=0.2): 0.6090
    * Qwen3-4B_rv6_03-14-n04_pv12 (4bit) (gen base): 0.4643
  * 모델
    * Qwen3-8B_rv7_03-15-n04_pv11 (original) (gen base): 0.6349
    * Qwen3-4B_rv7_03-15-n04_pv11 (original) (gen base): 0.6228
    * Qwen3-8B_rv7_03-15-n04_pv11 (4bit) (gen base): 0.6279
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen base): 0.6346
  * 하이퍼 파라미터
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen base): 0.6346
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (gen temp=0.4): 0.6137
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (token temp=0.4): 0.6233
    * Qwen3-4B_rv7_03-15-n04_pv11 (4bit) (default): 0.6340
  * 모델
    * Qwen/Qwen3-4B (4bit): 0.6340, 175분
    * Qwen/Qwen3-8B (4bit): 
    * skt/A.X-4.0-Light (4bit): 
    * LGAI-EXAONE/EXAONE-4.0-1.2B (4bit): 
    * kakaocorp/kanana-1.5-15.7b-a3b-instruct (4bit): bad


## 4060 기준 시간 측정
* time limit rule: 4090 기준 270분
* Final
  * --------------------------------------------------------------------------
  * L4 기준, Qwen 8B (original), BATCH_SIZE=1: 340분 예상 (L4), 260분 (A100)
  * L4 기준, Qwen 4B (original), BATCH_SIZE=4: 140분 예상 (L4), 102분 (A100)
  * L4 기준, Qwen 8B (4bit), BATCH_SIZE=8: 238분 예상 (L4), 123분 (A100)
  * L4 기준, Qwen 4B (4bit), BATCH_SIZE=16: 205분 예상 (L4), 203분 (A100)
  * --------------------------------------------------------------------------
  * L4 기준, BATCH_SIZE=1, Qwen 14B (original): OOM Fail (L4)
  * L4 기준, BATCH_SIZE=8, Qwen 14B (4bit): 470분 예상 타임 아웃 (L4)
* Qwen
  * Qwen/Qwen2.5-0.5B-Instruct: 3.2분
  * Qwen/Qwen3-0.6B: 3.2분
  * Qwen/Qwen3-1.7B (4bit): 6.4분
  * Qwen/Qwen3-1.7B: 3.6분
  * Qwen/Qwen3-4B: 43.1분 (예상) / 15.1분 (실제)
  * Qwen/Qwen3-8B: 180.7분 (예상) / 92.0분 (실제)
  * Qwen/Qwen3-14B: 471.0분 (예상) / 198.5분 (실제)
  * Qwen/Qwen3-4B (think): 183.8분 (예상)
  * Qwen/Qwen3-8B (think): X
  * Qwen/Qwen3-14B (think): X
* Korean
  * kakaocorp/kanana-1.5-8b-instruct-2505: 330.6분 (예상) / 92.7분 (실제)
  * skt/A.X-4.0-Light: 154.2분 (예상) / 64.9분 (실제)
  * K-intelligence/Midm-2.0-Base-Instruct: 294.9분 (예상) / 133.0분 (실제)
  * LGAI-EXAONE/EXAONE-4.0-1.2B: 1.07분 (예상) / 1.07분 (실제)
  * LGAI-EXAONE/EXAONE-4.0-1.2B (think): 148.3분 (예상) / 217.4분 (실제)
* Fin
  * TheFinAI/Fin-o1-8B: 168.0분 (예상)
  * TheFinAI/Fin-o1-14B: X
  * EleutherAI/polyglot-ko-5.8b: 39.5분 (예상)
  * EleutherAI/polyglot-ko-12.8b: X
  * KRAFTON/KORani-v1-13B: X
  * KRAFTON/KORani-v3-13B: X
* embedding
  * intfloat/multilingual-e5-base: 16분
  * Lajavaness/bilingual-embedding-base: 18분
  * Alibaba-NLP/gte-multilingual-base: 25분
  * HIT-TMG/KaLM-embedding-multilingual-mini-v1: 18분
