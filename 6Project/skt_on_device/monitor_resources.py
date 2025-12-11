#!/usr/bin/env python3
"""
vLLM API 서버의 GPU VRAM과 RAM 사용량을 모니터링하는 스크립트
"""

import argparse
import asyncio
import json
import logging
import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional

import aiohttp
import GPUtil
import psutil

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class ResourceMonitor:
    def __init__(self, server_pid: Optional[int] = None, api_url: str = "http://localhost:8000"):
        """
        리소스 모니터 초기화

        Args:
            server_pid: 모니터링할 서버 프로세스 ID (None이면 자동 감지)
            api_url: API 서버 URL
        """
        self.server_pid = server_pid
        self.api_url = api_url
        self.monitoring = False

        # 사용량 기록
        self.gpu_usage_history = []
        self.ram_usage_history = []
        self.vram_usage_history = []

        # Peak 값들
        self.peak_gpu_util = 0.0
        self.peak_vram_used = 0.0
        self.peak_ram_used = 0.0

        # 프로세스 정보
        self.process = None

    def find_server_process(self) -> Optional[psutil.Process]:
        """vLLM API 서버 프로세스를 찾습니다."""
        for proc in psutil.process_iter(["pid", "name", "cmdline"]):
            try:
                cmdline = proc.info["cmdline"]
                if cmdline and any("vllm_api_server" in cmd for cmd in cmdline):
                    logger.info(f"Found vLLM API server process: PID {proc.info['pid']}")
                    return psutil.Process(proc.info["pid"])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return None

    def get_gpu_info(self) -> Dict:
        """GPU 정보를 가져옵니다."""
        try:
            gpus = GPUtil.getGPUs()
            if not gpus:
                return {"available": False, "error": "No GPU found"}

            gpu_info = []
            total_vram_used = 0.0
            max_gpu_util = 0.0

            for gpu in gpus:
                gpu_data = {
                    "id": gpu.id,
                    "name": gpu.name,
                    "load": gpu.load * 100,  # GPU 사용률 (%)
                    "memory_used": gpu.memoryUsed,  # MB
                    "memory_total": gpu.memoryTotal,  # MB
                    "memory_util": (gpu.memoryUsed / gpu.memoryTotal) * 100,  # VRAM 사용률 (%)
                    "temperature": gpu.temperature,
                }
                gpu_info.append(gpu_data)
                total_vram_used += gpu.memoryUsed
                max_gpu_util = max(max_gpu_util, gpu.load * 100)

            return {
                "available": True,
                "gpus": gpu_info,
                "total_vram_used_mb": total_vram_used,
                "max_gpu_utilization": max_gpu_util,
            }
        except Exception as e:
            return {"available": False, "error": str(e)}

    def get_process_memory(self) -> Dict:
        """프로세스의 메모리 사용량을 가져옵니다."""
        try:
            if not self.process:
                return {"available": False, "error": "Process not found"}

            memory_info = self.process.memory_info()
            memory_percent = self.process.memory_percent()

            return {
                "available": True,
                "rss_mb": memory_info.rss / 1024 / 1024,  # MB
                "vms_mb": memory_info.vms / 1024 / 1024,  # MB
                "percent": memory_percent,
                "num_threads": self.process.num_threads(),
            }
        except Exception as e:
            return {"available": False, "error": str(e)}

    def get_system_memory(self) -> Dict:
        """시스템 메모리 정보를 가져옵니다."""
        try:
            memory = psutil.virtual_memory()
            return {
                "total_gb": memory.total / 1024 / 1024 / 1024,
                "used_gb": memory.used / 1024 / 1024 / 1024,
                "available_gb": memory.available / 1024 / 1024 / 1024,
                "percent": memory.percent,
            }
        except Exception as e:
            return {"error": str(e)}

    async def check_server_status(self) -> Dict:
        """API 서버 상태를 확인합니다."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.api_url}/stats", timeout=5) as response:
                    if response.status == 200:
                        stats = await response.json()
                        return {"available": True, "stats": stats}
                    else:
                        return {"available": False, "error": f"HTTP {response.status}"}
        except Exception as e:
            return {"available": False, "error": str(e)}

    def update_peaks(self, gpu_info: Dict, process_memory: Dict):
        """Peak 값들을 업데이트합니다."""
        if gpu_info.get("available"):
            self.peak_gpu_util = max(self.peak_gpu_util, gpu_info.get("max_gpu_utilization", 0))
            self.peak_vram_used = max(self.peak_vram_used, gpu_info.get("total_vram_used_mb", 0))

        if process_memory.get("available"):
            self.peak_ram_used = max(self.peak_ram_used, process_memory.get("rss_mb", 0))

    def save_history(self, timestamp: str, gpu_info: Dict, process_memory: Dict, system_memory: Dict):
        """사용량 히스토리를 저장합니다."""
        self.gpu_usage_history.append(
            {
                "timestamp": timestamp,
                "gpu_utilization": gpu_info.get("max_gpu_utilization", 0),
                "vram_used_mb": gpu_info.get("total_vram_used_mb", 0),
                "ram_used_mb": process_memory.get("rss_mb", 0),
                "system_ram_percent": system_memory.get("percent", 0),
            }
        )

    async def monitor_loop(self, interval: float = 1.0, duration: Optional[float] = None):
        """메인 모니터링 루프"""
        logger.info("=== 리소스 모니터링 시작 ===")

        # 프로세스 찾기
        if self.server_pid:
            try:
                self.process = psutil.Process(self.server_pid)
                logger.info(f"Monitoring process PID: {self.server_pid}")
            except psutil.NoSuchProcess:
                logger.error(f"Process with PID {self.server_pid} not found")
                return
        else:
            self.process = self.find_server_process()
            if not self.process:
                logger.error("vLLM API server process not found. Please specify PID manually.")
                return

        self.monitoring = True
        start_time = time.time()

        try:
            while self.monitoring:
                current_time = datetime.now()
                timestamp = current_time.isoformat()

                # 리소스 정보 수집
                gpu_info = self.get_gpu_info()
                process_memory = self.get_process_memory()
                system_memory = self.get_system_memory()
                server_status = await self.check_server_status()

                # Peak 값 업데이트
                self.update_peaks(gpu_info, process_memory)

                # 히스토리 저장
                self.save_history(timestamp, gpu_info, process_memory, system_memory)

                # 실시간 출력
                print(f"\r[{current_time.strftime('%H:%M:%S')}] ", end="")

                if gpu_info.get("available"):
                    print(
                        f"GPU: {gpu_info['max_gpu_utilization']:.1f}% | "
                        f"VRAM: {gpu_info['total_vram_used_mb']:.0f}MB | ",
                        end="",
                    )

                if process_memory.get("available"):
                    print(f"RAM: {process_memory['rss_mb']:.0f}MB | ", end="")

                print(
                    f"SysRAM: {system_memory.get('percent', 0):.1f}% | "
                    f"Server: {'✓' if server_status.get('available') else '✗'}",
                    end="",
                )

                # 지속 시간 체크
                if duration and (time.time() - start_time) >= duration:
                    break

                await asyncio.sleep(interval)

        except KeyboardInterrupt:
            logger.info("\nMonitoring interrupted by user")
        finally:
            self.monitoring = False
            print("\n")  # 줄바꿈

    def print_summary(self):
        """모니터링 결과 요약을 출력합니다."""
        logger.info("=== 모니터링 결과 요약 ===")
        logger.info(f"Peak GPU Utilization: {self.peak_gpu_util:.1f}%")
        logger.info(f"Peak VRAM Usage: {self.peak_vram_used:.0f} MB ({self.peak_vram_used/1024:.2f} GB)")
        logger.info(f"Peak RAM Usage: {self.peak_ram_used:.0f} MB ({self.peak_ram_used/1024:.2f} GB)")
        logger.info(f"Total monitoring duration: {len(self.gpu_usage_history)} samples")

    def save_report(self, output_file: str):
        """모니터링 결과를 파일로 저장합니다."""
        report = {
            "monitoring_info": {
                "start_time": self.gpu_usage_history[0]["timestamp"] if self.gpu_usage_history else None,
                "end_time": self.gpu_usage_history[-1]["timestamp"] if self.gpu_usage_history else None,
                "total_samples": len(self.gpu_usage_history),
                "server_pid": self.process.pid if self.process else None,
            },
            "peak_usage": {
                "gpu_utilization_percent": self.peak_gpu_util,
                "vram_used_mb": self.peak_vram_used,
                "vram_used_gb": self.peak_vram_used / 1024,
                "ram_used_mb": self.peak_ram_used,
                "ram_used_gb": self.peak_ram_used / 1024,
            },
            "usage_history": self.gpu_usage_history,
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        logger.info(f"모니터링 리포트가 {output_file}에 저장되었습니다.")


def signal_handler(signum, frame):
    """시그널 핸들러"""
    logger.info("Monitoring interrupted by signal")
    sys.exit(0)


async def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="vLLM API 서버 리소스 모니터링")

    parser.add_argument("--pid", type=int, help="모니터링할 서버 프로세스 ID")
    parser.add_argument("--url", type=str, default="http://localhost:8000", help="API 서버 URL")
    parser.add_argument("--interval", type=float, default=1.0, help="모니터링 간격(초)")
    parser.add_argument("--duration", type=float, help="모니터링 지속 시간(초). 미지정시 무한 실행")
    parser.add_argument("--output", type=str, default="monitoring_report.json", help="결과 저장 파일")
    parser.add_argument("--no-save", action="store_true", help="결과를 파일로 저장하지 않음")

    args = parser.parse_args()

    # 시그널 핸들러 등록
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("=== vLLM API 서버 리소스 모니터링 ===")
    logger.info(f"API URL: {args.url}")
    logger.info(f"모니터링 간격: {args.interval}초")
    if args.duration:
        logger.info(f"모니터링 지속 시간: {args.duration}초")
    else:
        logger.info("모니터링 지속 시간: 무제한 (Ctrl+C로 중단)")

    # 모니터 초기화 및 실행
    monitor = ResourceMonitor(server_pid=args.pid, api_url=args.url)

    try:
        await monitor.monitor_loop(interval=args.interval, duration=args.duration)
    finally:
        # 결과 출력 및 저장
        monitor.print_summary()

        if not args.no_save and monitor.gpu_usage_history:
            monitor.save_report(args.output)


if __name__ == "__main__":
    # 필요한 패키지 체크
    try:
        import aiohttp
        import GPUtil
        import psutil
    except ImportError as e:
        logger.error(f"Required package not found: {e}")
        logger.error("Please install: pip install GPUtil psutil aiohttp")
        sys.exit(1)

    asyncio.run(main())
