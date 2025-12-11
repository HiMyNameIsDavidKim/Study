#!/usr/bin/env python3
"""
vLLM API 클라이언트 테스트 스크립트
"""

import argparse
import asyncio
import json
import logging
import os
import time
from typing import Any, Dict, List, Optional

import aiohttp
import pandas as pd

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VLLMAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        vLLM API 클라이언트

        Args:
            base_url: API 서버 주소
        """
        self.base_url = base_url.rstrip("/")
        self.session = None

    async def __aenter__(self):
        """비동기 컨텍스트 매니저 진입"""
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """비동기 컨텍스트 매니저 종료"""
        if self.session:
            await self.session.close()

    async def predict_single(
        self, query: str, max_tokens: int = 50, temperature: float = 0.1, top_p: float = 0.9
    ) -> Dict[str, Any]:
        """단일 쿼리 예측"""
        payload = {"query": query, "max_tokens": max_tokens, "temperature": temperature, "top_p": top_p}

        async with self.session.post(f"{self.base_url}/predict", json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                error_text = await response.text()
                raise Exception(f"API 오류 ({response.status}): {error_text}")

    async def get_stats(self) -> Dict[str, Any]:
        """서버 통계"""
        async with self.session.get(f"{self.base_url}/stats") as response:
            return await response.json()


async def test_single_predictions(client: VLLMAPIClient):
    """단일 예측 테스트"""
    logger.info("=== 단일 예측 테스트 ===")

    test_queries = [
        "공기 청정기 켜줘",
        "스테이션으로 돌아가",
        "풍량 강풍으로 바꿔줘",
        "청정 기능 켜줘",
        "터보로 바꿔줘",
        "충전 해줘",
        "내일 프라하 TVOC 농도는 얼마야",
    ]

    results = []
    total_time = 0

    for query in test_queries:
        start_time = time.time()
        try:
            result = await client.predict_single(query)
            request_time = (time.time() - start_time) * 1000
            total_time += request_time

            logger.info(f"Query: {query}")
            logger.info(f"Prediction: {result['prediction']}")
            logger.info(f"Inference Time: {result['inference_time_ms']:.2f}ms")
            logger.info(f"Request Time: {request_time:.2f}ms")
            logger.info(f"Tokens/sec: {result['tokens_per_second']:.2f}")
            logger.info("-" * 60)

            results.append(
                {
                    "query": query,
                    "prediction": result["prediction"],
                    "inference_time_ms": result["inference_time_ms"],
                    "request_time_ms": request_time,
                    "tokens_per_second": result["tokens_per_second"],
                }
            )

        except Exception as e:
            logger.error(f"Query '{query}' 실패: {str(e)}")

    avg_inference_time = sum(r["inference_time_ms"] for r in results) / len(results)
    avg_request_time = total_time / len(results)

    logger.info(f"단일 예측 테스트 완료")
    logger.info(f"평균 추론 시간: {avg_inference_time:.2f}ms")
    logger.info(f"평균 요청 시간: {avg_request_time:.2f}ms")

    return results


async def benchmark_performance(
    client: VLLMAPIClient,
    bench_data_path: str,
    num_requests: int = 10,
    min_chars: Optional[int] = None,
    max_chars: Optional[int] = None,
):
    """성능 벤치마크"""
    logger.info(f"=== 성능 벤치마크 ({num_requests}회 요청) ===")

    df = pd.read_csv(bench_data_path, encoding="utf-8", index_col=0)
    test_query_list = df["Query(한글)"].tolist()
    test_query_count = len(test_query_list)

    if min_chars:
        test_query_list = [query for query in test_query_list if len(query) >= min_chars]
    if max_chars:
        test_query_list = [query for query in test_query_list if len(query) <= max_chars]

    single_times = []
    for i in range(num_requests):
        start_time = time.time()
        try:
            result = await client.predict_single(test_query_list[i % test_query_count])
            request_time = (time.time() - start_time) * 1000
            single_times.append(
                {
                    "request_time": request_time,
                    "inference_time": result["inference_time_ms"],
                    "tokens_per_second": result["tokens_per_second"],
                }
            )
            logger.info(f"요청 {i+1}/{num_requests}: {request_time:.2f}ms")
        except Exception as e:
            logger.error(f"요청 {i+1} 실패: {str(e)}")

    if single_times:
        avg_request_time = sum(t["request_time"] for t in single_times) / len(single_times)
        avg_inference_time = sum(t["inference_time"] for t in single_times) / len(single_times)
        avg_tokens_per_sec = sum(t["tokens_per_second"] for t in single_times) / len(single_times)

        logger.info(f"단일 요청 평균 결과:")
        logger.info(f"  요청 시간: {avg_request_time:.2f}ms")
        logger.info(f"  추론 시간: {avg_inference_time:.2f}ms")
        logger.info(f"  토큰/초: {avg_tokens_per_sec:.2f}")

    return single_times


async def test_audio_prediction(client: VLLMAPIClient, audio_file_or_folder: str):
    """오디오 예측 테스트"""
    logger.info(f"=== 오디오 예측 테스트: {audio_file_or_folder} ===")

    if not os.path.exists(audio_file_or_folder):
        logger.error(f"오디오 파일이 없습니다: {audio_file_or_folder}")
        return

    url = f"{client.base_url}/predict_audio"

    if os.path.isdir(audio_file_or_folder):
        for root, dirs, files in os.walk(audio_file_or_folder):
            for file in files:
                try:
                    with open(os.path.join(root, file), "rb") as f:
                        form = aiohttp.FormData()
                        form.add_field(
                            name="file",
                            value=f,
                            filename=os.path.basename(os.path.join(root, file)),
                            content_type="audio/wav",
                        )
                        async with client.session.post(url, data=form) as response:
                            if response.status == 200:
                                result = await response.json()
                                logger.info(f"Transcribed Text: {result['transcribed_text']}")
                                logger.info(f"Prediction: {result['prediction']}")
                                logger.info(f"Total Inference Time: {result['total_inference_time_ms']:.2f}ms")
                                logger.info("-" * 60)
                            else:
                                error_text = await response.text()
                                logger.error(f"API 오류 ({response.status}): {error_text}")
                except Exception as e:
                    logger.error(f"오디오 예측 실패: {str(e)}")


async def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="vLLM API 클라이언트 테스트")

    parser.add_argument("--api_url", type=str, default="http://localhost:8000", help="API 서버 URL")

    parser.add_argument(
        "--test_type",
        type=str,
        choices=["single", "benchmark", "audio", "all"],
        default="all",
        help="테스트 타입",
    )

    parser.add_argument("--audio_path", type=str, help="테스트할 오디오 파일 경로")
    parser.add_argument("--num_requests", type=int, default=10, help="벤치마크 요청 수")

    args = parser.parse_args()

    async with VLLMAPIClient(args.api_url) as client:
        try:
            # 테스트 실행
            if args.test_type in ["single", "all"]:
                await test_single_predictions(client)
                logger.info("")

            if args.test_type in ["benchmark", "all"]:
                await benchmark_performance(client, "/mnt/elice/dataset/train_data.csv", args.num_requests)
                logger.info("")

            if args.test_type in ["audio", "all"] and args.audio_path:
                await test_audio_prediction(client, args.audio_path)
                logger.info("")

            # 최종 통계
            logger.info("=== 서버 통계 ===")
            stats = await client.get_stats()
            logger.info(f"업타임: {stats['uptime_seconds']:.2f}초")
            logger.info(f"모델 로드 상태: {stats['model_loaded']}")

        except Exception as e:
            logger.error(f"테스트 실행 중 오류: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
