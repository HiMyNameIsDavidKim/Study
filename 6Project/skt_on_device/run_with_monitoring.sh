#!/bin/bash

# vLLM API 서버를 모니터링과 함께 실행하는 스크립트

set -e

# 기본 설정
HOST="0.0.0.0"
PORT="8000"
MONITOR_INTERVAL="1.0"
OUTPUT_DIR="monitoring_results"

# 사용법 출력
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --host HOST          서버 호스트 (기본값: $HOST)"
    echo "  --port PORT          서버 포트 (기본값: $PORT)"
    echo "  --interval SECONDS   모니터링 간격 (기본값: $MONITOR_INTERVAL)"
    echo "  --output-dir DIR     결과 저장 디렉토리 (기본값: $OUTPUT_DIR)"
    echo "  --no-monitor         모니터링 없이 서버만 실행"
    echo "  --monitor-only       기존 서버 모니터링만 실행"
    echo "  --help               이 도움말 출력"
    echo ""
    echo "예시:"
    echo "  $0                                    # 기본 설정으로 실행"
    echo "  $0 --port 8080 --interval 0.5        # 포트와 모니터링 간격 지정"
    echo "  $0 --monitor-only                     # 기존 서버 모니터링만"
    echo ""
    exit 1
}

# 인자 파싱
MONITOR_ENABLED=true
MONITOR_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --host)
            HOST="$2"
            shift 2
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        --interval)
            MONITOR_INTERVAL="$2"
            shift 2
            ;;
        --output-dir)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --no-monitor)
            MONITOR_ENABLED=false
            shift
            ;;
        --monitor-only)
            MONITOR_ONLY=true
            shift
            ;;
        --help)
            usage
            ;;
        *)
            echo "알 수 없는 옵션: $1"
            usage
            ;;
    esac
done

# 필요한 파일 확인
check_files() {
    local files=("vllm_api_server.py" "monitor_resources.py")
    for file in "${files[@]}"; do
        if [[ ! -f "$file" ]]; then
            echo "오류: $file 파일을 찾을 수 없습니다."
            exit 1
        fi
    done
}

# 모니터링 결과 디렉토리 생성
setup_output_dir() {
    mkdir -p "$OUTPUT_DIR"
    echo "모니터링 결과 저장 위치: $OUTPUT_DIR"
}

# 서버 프로세스 ID 찾기
find_server_pid() {
    local pid=$(pgrep -f "vllm_api_server.py" | head -1)
    echo "$pid"
}

# 정리 함수
cleanup() {
    echo ""
    echo "정리 중..."
    
    if [[ -n "$SERVER_PID" ]]; then
        echo "API 서버 종료 중... (PID: $SERVER_PID)"
        kill $SERVER_PID 2>/dev/null || true
        wait $SERVER_PID 2>/dev/null || true
    fi
    
    if [[ -n "$MONITOR_PID" ]]; then
        echo "모니터링 종료 중... (PID: $MONITOR_PID)"
        kill $MONITOR_PID 2>/dev/null || true
        wait $MONITOR_PID 2>/dev/null || true
    fi
    
    echo "정리 완료"
    exit 0
}

# 시그널 핸들러 설정
trap cleanup SIGINT SIGTERM

# 메인 로직
main() {
    echo "=== vLLM API 서버 + 모니터링 실행 스크립트 ==="
    
    check_files
    
    if [[ "$MONITOR_ENABLED" == "true" ]]; then
        setup_output_dir
    fi
    
    # 모니터링만 실행하는 경우
    if [[ "$MONITOR_ONLY" == "true" ]]; then
        echo "기존 서버 모니터링 모드"
        
        local existing_pid=$(find_server_pid)
        if [[ -z "$existing_pid" ]]; then
            echo "오류: 실행 중인 vLLM API 서버를 찾을 수 없습니다."
            exit 1
        fi
        
        echo "발견된 서버 PID: $existing_pid"
        echo "모니터링 시작..."
        
        python monitor_resources.py \
            --pid "$existing_pid" \
            --interval "$MONITOR_INTERVAL" \
            --url "http://localhost:$PORT" \
            --output "$OUTPUT_DIR/monitoring_$(date +%Y%m%d_%H%M%S).json"
        
        return
    fi
    
    # 서버 시작
    echo "API 서버 시작 중..."
    echo "Host: $HOST"
    echo "Port: $PORT"
    
    python vllm_api_server.py --host "$HOST" --port "$PORT" &
    SERVER_PID=$!
    
    echo "서버 PID: $SERVER_PID"
    
    # 서버 시작 대기
    echo "서버 시작 대기 중..."
    sleep 10
    
    # 서버 상태 확인
    if ! kill -0 $SERVER_PID 2>/dev/null; then
        echo "오류: 서버 시작에 실패했습니다."
        exit 1
    fi
    
    # 모니터링 시작 (활성화된 경우)
    if [[ "$MONITOR_ENABLED" == "true" ]]; then
        echo "모니터링 시작..."
        echo "모니터링 간격: ${MONITOR_INTERVAL}초"
        
        local timestamp=$(date +%Y%m%d_%H%M%S)
        python monitor_resources.py \
            --pid "$SERVER_PID" \
            --interval "$MONITOR_INTERVAL" \
            --url "http://localhost:$PORT" \
            --output "$OUTPUT_DIR/monitoring_$timestamp.json" &
        
        MONITOR_PID=$!
        echo "모니터링 PID: $MONITOR_PID"
    fi
    
    echo ""
    echo "=== 실행 중 ==="
    echo "API 서버: http://localhost:$PORT"
    if [[ "$MONITOR_ENABLED" == "true" ]]; then
        echo "모니터링: 활성화 (PID: $MONITOR_PID)"
        echo "결과 저장: $OUTPUT_DIR/"
    else
        echo "모니터링: 비활성화"
    fi
    echo ""
    echo "종료하려면 Ctrl+C를 누르세요."
    
    # 메인 루프 (서버 프로세스 대기)
    wait $SERVER_PID
}

# 스크립트 실행
main