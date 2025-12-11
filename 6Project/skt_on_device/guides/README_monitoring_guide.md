# 리소스 모니터링 가이드

이 가이드는 vLLM API 서버의 GPU VRAM과 RAM 사용량을 모니터링하는 방법을 설명합니다.

## 빠른 시작

### 1. 자동 실행 (권장)

```bash
# 이미 실행중인 서버를 모니터링 (권장)
bash run_with_monitoring.sh --monitor-only

# 새로운 서버를 실행한 후 모니터링
bash run_with_monitoring.sh 

```

### 2. 수동 실행

```bash
# 터미널 1: API 서버 실행
python vllm_api_server.py

# 터미널 2: 모니터링 실행
python monitor_resources.py
```

## 상세 사용법

### 모니터링 스크립트 옵션

```bash
python monitor_resources.py [OPTIONS]
```

```bash
옵션:
  --pid PID                 # 모니터링할 프로세스 ID (입력하지 않을 시 자동 감지)
  --url URL                 #API 서버 URL (기본값: <http://localhost:8000>)
  --interval SECONDS        #모니터링 간격 (기본값: 1.0초)
  --duration SECONDS        #모니터링 지속 시간 (기본값: 무제한)
  --output FILE             #결과 저장 파일 (기본값: monitoring_report.json)
  --no-save                 #결과를 파일로 저장하지 않음
```

### 사용 예시

#### 기본 모니터링

```bash
python monitor_resources.py
```

#### 특정 프로세스 모니터링

```bash
python monitor_resources.py --pid 12345
```

#### 세밀한 모니터링 (0.5초 간격)

```bash
python monitor_resources.py --interval 0.5
```

#### 30초간 모니터링 후 자동 종료

```bash
python monitor_resources.py --duration 30
```

#### 특정 파일에 결과 저장

```bash
python monitor_resources.py --output my_test_result.json
```

## 모니터링 출력 해석

### 실시간 출력

```
[14:30:15] GPU: 85.2% | VRAM: 3240MB | RAM: 1580MB | SysRAM: 45.3% | Server: ✓
```

- **GPU**: GPU 사용률 (%)
- **VRAM**: GPU 메모리 사용량 (MB)
- **RAM**: 프로세스 RAM 사용량 (MB)
- **SysRAM**: 시스템 전체 RAM 사용률 (%)
- **Server**: API 서버 상태 (✓: 정상, ✗: 비활성화)

### 최종 요약

```
=== 모니터링 결과 요약 ===
Peak GPU Utilization: 92.3%
Peak VRAM Usage: 3580 MB (3.49 GB)
Peak RAM Usage: 1650 MB (1.61 GB)
Total monitoring duration: 300 samples
```

## JSON 리포트 구조

```json
{
  "monitoring_info": {
    "start_time": "2024-01-01T14:30:00",
    "end_time": "2024-01-01T14:35:00",
    "total_samples": 300,
    "server_pid": 12345
  },
  "peak_usage": {
    "gpu_utilization_percent": 92.3,
    "vram_used_mb": 3580,
    "vram_used_gb": 3.49,
    "ram_used_mb": 1650,
    "ram_used_gb": 1.61
  },
  "usage_history": [
    {
      "timestamp": "2024-01-01T14:30:00",
      "gpu_utilization": 85.2,
      "vram_used_mb": 3240,
      "ram_used_mb": 1580,
      "system_ram_percent": 45.3
    },
    ...
  ]
}
```

## 성능 분석 시나리오

### 1. 모델 로딩 시 리소스 사용량

```bash
# 1단계: 모니터링 시작
python monitor_resources.py --output model_loading.json &

# 2단계: 서버 시작 (별도 터미널)
python vllm_api_server.py

# 3단계: 모델 로딩 완료 후 모니터링 중단 (Ctrl+C)
```

**분석 포인트:**

- 모델 로딩 시작 시점에서 VRAM 급증
- 로딩 완료 후 VRAM 안정화
- 초기 RAM 사용량 확인

### 2. 추론 시 Peak 사용량 측정

```bash
# 1단계: 장시간 모니터링 시작
python monitor_resources.py --duration 600 --output inference_peak.json &

# 2단계: 다양한 부하 테스트 (별도 터미널)
python api_client.py --test_type single
python api_client.py --test_type benchmark --num_requests 100
python api_client.py --test_type audio --audio_path train_data_sample/audio
```

### 3. 연속 운영 시 안정성 확인

```bash
# 장시간 모니터링 (1시간)
python monitor_resources.py --interval 5 --duration 3600 --output stability_test.json
```

**분석 포인트:**

- 메모리 누수 여부 확인
- 시간에 따른 성능 변화
- 시스템 안정성

## 최적화 팁

### 1. 모니터링 오버헤드 최소화

- 간격을 너무 짧게 설정하지 마세요 (권장: 1초 이상)
- 장시간 모니터링 시 간격을 늘리세요 (5-10초)

### 2. 디스크 공간 관리

- 히스토리 데이터가 많으면 파일이 커집니다
- 필요시 `--no-save` 옵션으로 파일 저장 비활성화

### 3. 백그라운드 실행

```bash
# 백그라운드에서 실행하고 로그 저장
nohup python monitor_resources.py --output monitor.json > monitor.log 2>&1 &
```
