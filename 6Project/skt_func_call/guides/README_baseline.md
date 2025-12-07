# Baseline 코드

Baseline 코드는 meta-llama/Llama-3.2-1B-Instruct 모델을 바탕으로 별도의 파인 튜닝 없이 Function Calling을 수행하는 코드입니다.

## 1. 코드 구조

코드 구조는 아래와 같습니다.

```
baseline/
├── api_endpoint.txt          # API 서버 엔드포인트 설정 파일
├── guides/                   # 사용 가이드 문서들
│   ├── README_baseline.md           # 베이스라인 시스템 전체 가이드
│   ├── README_monitoring_guide.md   # 리소스 모니터링 사용법
│   ├── README_sync.md               # 파일 동기화 관련 가이드
│   └── README_vLLM_API_server.md   # vLLM API 서버 설정 및 사용법
├── inference.py              # AI 모델 추론 실행 메인 파일
├── monitor_resources.py      # GPU/CPU/메모리 사용량 모니터링 스크립트
├── references/               # 참고 자료 및 예제 코드
│   ├── llama_finetune.py     # 파인튜닝 스크립트
│   ├── peft_merger.py        # PEFT 모델 병합 스크립트
│   └── run_training.py       # 파인튜닝 관리 스크립트
├── requirements.txt          # Python 패키지 의존성 목록
├── run_with_monitoring.sh   # 모니터링과 함께 API 서버를 실행하는 스크립트
├── stt_processor.py         # SenseVoice STT 모델 기반 음성-텍스트 변환(STT) 처리기
└── vllm_api_server.py       # vLLM 기반 추론 API 서버
```

Baseline 코드 중 `vllm_api_server.py` 스크립트는 모델을 호스팅하는 API 서버를 실행하는 스크립트입니다. 이 스크립트를 실행하면 모델을 호스팅하는 API 서버가 실행됩니다.

## 2. baseline 서버 실행

아무런 학습을 하지 않은 모델을 실행하는 서버를 실행하려면 터미널에서 아래 명령어를 입력해주세요.

```
python vllm_api_server.py  --gpu_memory_utilization 0.1
```

이 명령어를 통해 실행한 API는 VRAM 제한을 초과하므로 검증 과정에서 실격 처리 될 수 있습니다. 양자화를 비롯한 여러 메모리 절약 기법을 적용하여 메모리 제한을 초과하지 않도록 해주세요.

스크립트의 구조 및 기초적인 사용법은 `guides/README_VLLM_API_server.md` 파일을 참고해주세요.

## 3. 응답 추출 로직 수정

baseline 코드의 입력 생성 및 응답 추출 로직은 각각 `vllm_api_server.py` 파일의 `create_prompt` 함수와 `extract_response` 함수에 구현되어 있습니다.

만약 다른 모델을 사용할 경우 프롬프트 생성 및 응답 추출 로직을 수정해주세요.

## 4. baseline 환경

baseline 환경에 설치된 라이브러리는 `baseline/guides/requirements.txt` 파일을 참고해주세요.
