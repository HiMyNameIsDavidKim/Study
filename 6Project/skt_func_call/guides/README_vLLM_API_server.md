# vLLM API 서버 가이드

양자화된 Llama 3.2 모델을 vLLM으로 서빙하는 API 서버 사용법을 설명합니다.

## 1. 환경 변수 설정 (.env 파일)

```bash
# 모델 경로
MODEL_PATH=./llama_function_call_merged

# API 설정
API_HOST=0.0.0.0
API_PORT=8000
```

## 2. 서버 실행

### 2.1. 기본 실행

```bash
python vllm_api_server.py
```

### 2.2. 커스텀 설정으로 실행

```bash
python vllm_api_server.py \
    --model_name ./llama_function_call_merged \
    --host 0.0.0.0 \
    --port 8000 \
    --gpu_memory_utilization 0.8 \
    --max_model_len 512
```

### 2.3. 백그라운드 실행

```bash
nohup python vllm_api_server.py > vllm_server.log 2>&1 &
```

## 3. API 엔드포인트

### 3.1. 단일 쿼리 예측

```bash
POST /predict
```

**요청 본문:**

```json
{
  "query": "공기 청정기 켜줘",
  "max_tokens": 50,
  "temperature": 0.1,
  "top_p": 0.9
}
```

**응답 예시:**

```json
{
  "query": "공기 청정기 켜줘",
  "prediction": "<sk_0>()<sk_end>",
  "inference_time_ms": 45.2,
  "tokens_per_second": 22.1,
  "timestamp": "2024-01-01T12:00:00"
}
```

### 3.2. 음성 데이터 쿼리 예측

```bash
POST /predict_audio
```

**요청 본문:**

```json
{
  "file": {
    "filename": "audio.wav",
    "content_type": "audio/wav",
    "body": "base64_encoded_audio_data"
  },
  "max_tokens": 50,
  "temperature": 0.1,
  "top_p": 0.9
}
```

**응답 예시:**

```json
{
  "transcribed_text": "공기 청정기 켜줘",
  "prediction": "<sk_0>()<sk_end>",
  "stt_inference_time_ms": 45.2,
  "llm_inference_time_ms": 45.2,
  "total_inference_time_ms": 90.4,
  "timestamp": "2024-01-01T12:00:00"
}
```

## 4. API 테스트

### 4.1. cURL을 사용한 직접 테스트

```bash
# 단일 예측
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"query": "공기 청정기 켜줘"}'

# 음성 데이터 예측
curl -X POST http://localhost:8000/predict_audio \
  -F "file=@audio.wav"
```

### 4.2. Python requests 사용 예시

```python
import requests
import json

# API 서버 URL
api_url = "http://localhost:8000"

# 단일 예측
response = requests.post(
    f"{api_url}/predict",
    json={"query": "공기 청정기 켜줘"}
)
result = response.json()
print(f"예측 결과: {result['prediction']}")
print(f"추론 시간: {result['inference_time_ms']:.2f}ms")

# 음성 데이터 예측
response = requests.post(
    f"{api_url}/predict_audio",
    files={"file": (os.path.basename(audio_path), f, "audio/wav")}
)
result = response.json()
print(f"예측 결과: {result['prediction']}")
# 채점 기준은 이 추론 시간 값이 아니라 request를 보내기 시작한 시점과 response가 도착한 시점 사이의 시간을 측정하여 채점합니다.
print(f"추론 시간: {result['total_inference_time_ms']:.2f}ms")
```

## 5. 성능 모니터링

### 5.1. 실시간 로그 모니터링

```bash
# 서버 로그 실시간 확인
tail -f vllm_server.log

# 특정 키워드 필터링
tail -f vllm_server.log | grep "예측 완료"
```

### 5.2. 성능 지표 확인

- **추론 시간 (Inference Time)**: 순수 모델 추론에 소요된 시간
- **요청 시간 (Request Time)**: 네트워크 + 처리 시간 포함
- **토큰/초 (Tokens per Second)**: 생성 속도 지표
- **처리량 (Throughput)**: 단위 시간당 처리 가능한 요청 수

### 5.3. 시스템 리소스 모니터링

```bash
# GPU 사용률 확인
nvidia-smi -l 1

# 메모리 사용량 확인
htop

# 네트워크 사용량 확인
iftop
```

## 6. 고급 설정

### 6.1. vLLM 엔진 설정

```python
# 서버 시작 시 환경 변수로 설정 가능
export VLLM_GPU_MEMORY_UTILIZATION=0.9
export VLLM_MAX_MODEL_LEN=512
export VLLM_TENSOR_PARALLEL_SIZE=1
```

### 6.2. 성능 튜닝

```bash
# GPU 메모리 사용률 조정 (0.8 = 80%)
python vllm_api_server.py --gpu_memory_utilization 0.8

# 최대 모델 길이 증가 (메모리 사용량 증가)
python vllm_api_server.py --max_model_len 1024
```

## 7. 문제 해결

### 7.1. 일반적인 문제들

**모델 로딩 실패**

```bash
# 모델 경로 확인
ls -la ./llama_function_call_merged

# 권한 확인
chmod -R 755 ./llama_function_call_merged
```

**포트 충돌**

```bash
# 다른 포트 사용
python vllm_api_server.py --port 8001

# 포트 사용 중인 프로세스 확인
lsof -i :8000
```

### 7.3. 로그 분석

```bash
# 에러 로그만 확인
grep "ERROR" vllm_server.log

# 성능 로그 확인
grep "예측 완료" vllm_server.log | tail -10
```

### 7.4. 디버깅 모드

```bash
# 디버그 로그 활성화
python vllm_api_server.py --log_level DEBUG
```

## 8. 성능 벤치마크

### 8.1. 벤치마크 실행

```bash
# 성능 테스트 실행
python api_client.py --test_type benchmark --num_requests 100

# 음성 테스트 실행
python api_client.py --test_type audio --audio_path train_data_sample/audio

# 결과 분석
grep "평균" api_client.log
```

## 9. 응답 추출 로직 수정

baseline 코드의 입력 생성 및 응답 추출 로직은 각각 `vllm_api_server.py` 파일의 `create_prompt` 함수와 `extract_response` 함수에 구현되어 있습니다.

만약 다른 모델을 사용할 경우 프롬프트 생성 및 응답 추출 로직을 수정해주세요.
