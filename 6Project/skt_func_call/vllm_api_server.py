#!/usr/bin/env python3
"""
vLLM과 SenseVoice를 사용한 음성-Function Call API 서버 (베이스라인)
"""

import argparse
import asyncio
import json
import logging
import os
import shutil
import time
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Optional
import re
import io
import librosa

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

# STT import
from stt_processor import SenseVoiceSTT
from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess

# vLLM imports
from vllm import SamplingParams
from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.engine.async_llm_engine import AsyncLLMEngine

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Global variables
llm_engine: Optional[AsyncLLMEngine] = None
# stt_processor: Optional[SenseVoiceSTT] = None
stt_processor: Optional[SenseVoiceSmall] = None


class QueryRequest(BaseModel):
    """단일 쿼리 요청 모델"""

    query: str = Field(..., description="사용자 명령")
    max_tokens: int = Field(50, description="최대 생성 토큰 수")
    temperature: float = Field(0.1, description="샘플링 온도")
    top_p: float = Field(0.9, description="Top-p 샘플링")


class InferenceResponse(BaseModel):
    """추론 응답 모델"""

    query: str
    prediction: str
    inference_time_ms: float
    tokens_per_second: float
    timestamp: str


class AudioInferenceResponse(BaseModel):
    """오디오 추론 응답 모델"""

    transcribed_text: str
    prediction: str
    stt_inference_time_ms: float
    llm_inference_time_ms: float
    total_inference_time_ms: float
    timestamp: str


# 서버 시작 시간
server_start_time = time.time()


# 환경 변수에서 설정 읽기
def get_model_config():
    """환경 변수에서 모델 설정을 읽어옵니다."""
    return {
        "model_name": os.getenv(
            "VLLM_MODEL_NAME", "~/.cache/huggingface/hub/models--meta-llama--Llama-3.2-1B-Instruct"
        ),
        "gpu_memory_utilization": float(os.getenv("VLLM_GPU_MEMORY_UTILIZATION", "0.020")),
        "max_model_len": int(os.getenv("VLLM_MAX_MODEL_LEN", "128")),
        "tensor_parallel_size": int(os.getenv("VLLM_TENSOR_PARALLEL_SIZE", "1")),
        "max_num_batched_tokens": int(os.getenv("VLLM_MAX_NUM_BATCHED_TOKENS", "128")),
        "max_num_seqs": int(os.getenv("VLLM_MAX_NUM_SEQS", "1")),
        "kv_cache_dtype": os.getenv("VLLM_KV_CACHE_DTYPE", "fp8_e5m2"),
        "enforce_eager": os.getenv("VLLM_ENFORCE_EAGER", "true").lower() == "true",
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 생명주기 관리"""
    # 서버 시작 시 모델 로드
    await load_models()
    yield
    # 서버 종료 시 정리
    await cleanup_models()


async def load_models():
    """모델들을 로드합니다."""
    global llm_engine, stt_processor

    logger.info("=== 모델 로딩 시작 ===")

    # vLLM 엔진 설정
    config = get_model_config()
    logger.info(f"vLLM 설정: {config}")

    # vLLM 엔진 초기화
    engine_args_dict = {
        "model": config["model_name"],
        "tokenizer": config["model_name"],
        "tensor_parallel_size": config["tensor_parallel_size"],
        "gpu_memory_utilization": config["gpu_memory_utilization"],
        "max_model_len": config["max_model_len"],
        "trust_remote_code": True,
        "max_num_batched_tokens": config["max_num_batched_tokens"],
        "max_num_seqs": config["max_num_seqs"],
        "kv_cache_dtype": config["kv_cache_dtype"],
        "enforce_eager": config["enforce_eager"],
    }

    engine_args = AsyncEngineArgs(**engine_args_dict)

    llm_engine = AsyncLLMEngine.from_engine_args(engine_args)
    logger.info("vLLM 엔진 로드 완료")

    # STT 모델 로드
    try:
        # stt_processor = SenseVoiceSTT()
        model_dir = "iic/SenseVoiceSmall"
        stt_processor = SenseVoiceSmall(
            model_dir,
            batch_size=1,
            quantize=True,
            # device_id="0",
            disable_update=True,
        )
        logger.info("STT 모델 로드 완료")
    except Exception as e:
        logger.warning(f"STT 모델 로드 실패: {e}")
        stt_processor = None

    logger.info("=== 모델 로딩 완료 ===")


async def cleanup_models():
    """모델들을 정리합니다."""
    global llm_engine, stt_processor

    logger.info("=== 모델 정리 시작 ===")

    if llm_engine:
        await llm_engine.shutdown()
        logger.info("vLLM 엔진 정리 완료")

    if stt_processor:
        del stt_processor
        stt_processor = None
        logger.info("STT 모델 정리 완료")

    logger.info("=== 모델 정리 완료 ===")


# 이 프롬프트는 llama 3.2 모델에 맞춰진 프롬프트입니다.
# 다른 모델을 사용할 경우 프롬프트를 수정해주세요.
def create_prompt(query: str) -> str:
    """프롬프트를 생성합니다."""
    return f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Convert Korean STT to `<function_identifier>()<end>` format. Fix errors like 배를린→베를린.
Main Functions: MO=날씨, IO=공기질, PG=청정/공청, QD=감지, BS=고스트/방해금지
<|eot_id|><|start_header_id|>user<|end_header_id|>
{query}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""


# 이 함수는 llama 3.2 프롬프트 양식에 맞춰진 함수입니다.
# 다른 모델을 사용할 경우 추출 로직을 수정해주세요.
def extract_response(generated_text: str) -> str:
    """생성된 텍스트에서 응답 부분을 추출합니다."""
    response = re.sub(r'"', '""', generated_text)
    return response



# FastAPI 앱 생성
app = FastAPI(
    title="Llama Function Call API (Baseline)",
    root_path="/proxy/8000",
    description="Llama 3.2-1B 모델을 사용한 Function Call API 서버",
    version="1.0.0",
    lifespan=lifespan,
)


@app.post(
    "/predict_audio",
    response_model=AudioInferenceResponse,
    summary="오디오 파일(STT+LLM) 예측",
)
async def predict_audio(
    file: UploadFile = File(description="오디오 파일 업로드 (wav, mp3 등), Grader는 이 field만 사용합니다."),
    max_tokens: int = Form(50, description="Grader는 이 field는 무시합니다."),
    temperature: float = Form(0.1, description="Grader는 이 field는 무시합니다."),
    top_p: float = Form(0.9, description="Grader는 이 field는 무시합니다."),
):
    """오디오 파일을 받아서 STT 후 Function Call을 예측합니다."""
    if not stt_processor:
        raise HTTPException(status_code=500, detail="STT 모델이 로드되지 않았습니다.")

    if not llm_engine:
        raise HTTPException(status_code=500, detail="LLM 엔진이 로드되지 않았습니다.")

    # 오디오 파일 처리
    audio_data = None
    if file:
        audio_data = await file.read()
        file_extension = file.filename.split(".")[-1] if file.filename else "wav"
    else:
        raise HTTPException(status_code=400, detail="오디오 파일이 제공되지 않았습니다.")

    # 임시 파일 생성
    # temp_file_path = f"/tmp/audio_{uuid.uuid4()}.{file_extension}"
    try:
        # with open(temp_file_path, "wb") as f:
        #     f.write(audio_data)

        # STT 처리
        stt_start_time = time.time()
        # transcribed_text = stt_processor.transcribe(temp_file_path)
        audio_buffer = io.BytesIO(audio_data)
        audio_array, sr = librosa.load(audio_buffer, sr=16000, mono=True)

        # 노이즈 전처리

        transcribed_text = stt_processor(audio_array, language="ko", use_itn=True)
        transcribed_text = rich_transcription_postprocess(transcribed_text[0])
        stt_time = (time.time() - stt_start_time) * 1000

        # LLM 추론
        llm_start_time = time.time()
        prompt = create_prompt(transcribed_text)

        sampling_params = SamplingParams(
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=["<end>"],
            include_stop_str_in_output=True,
        )

        request_id = f"audio_{int(time.time())}_{uuid.uuid4().hex}"

        results_generator = llm_engine.generate(prompt, sampling_params, request_id)
        final_output = None
        async for request_output in results_generator:
            final_output = request_output

        llm_time = (time.time() - llm_start_time) * 1000
        total_time = stt_time + llm_time

        prediction = final_output.outputs[0].text
        # prediction = extract_response(prediction)

        return AudioInferenceResponse(
            transcribed_text=transcribed_text,
            prediction=prediction,
            stt_inference_time_ms=stt_time,
            llm_inference_time_ms=llm_time,
            total_inference_time_ms=total_time,
            timestamp=datetime.now().isoformat(),
        )


    finally:
        # 임시 파일 정리
        # if os.path.exists(temp_file_path):
        #     os.remove(temp_file_path)
        pass



@app.post("/predict", response_model=InferenceResponse)
async def predict_single(request: QueryRequest):
    """단일 텍스트 쿼리에 대한 Function Call을 예측합니다."""
    if not llm_engine:
        raise HTTPException(status_code=500, detail="LLM 엔진이 로드되지 않았습니다.")

    start_time = time.time()

    prompt = create_prompt(request.query)

    sampling_params = SamplingParams(
        max_tokens=request.max_tokens,
        temperature=request.temperature,
        top_p=request.top_p,
        stop=["<end>"],
        include_stop_str_in_output=True,
    )

    request_id = f"text_{int(time.time())}_{uuid.uuid4().hex}"
    results_generator = llm_engine.generate(prompt, sampling_params, request_id)
    final_output = None
    async for request_output in results_generator:
        final_output = request_output

    generated_text = final_output.outputs[0].text
    prediction = extract_response(generated_text)

    inference_time = (time.time() - start_time) * 1000

    # 토큰 통계 계산
    tokens_per_second = 0
    if final_output.outputs[0].token_ids:
        num_tokens = len(final_output.outputs[0].token_ids)
        if inference_time > 0:
            tokens_per_second = (num_tokens / inference_time) * 1000

    return InferenceResponse(
        query=request.query,
        prediction=prediction,
        inference_time_ms=inference_time,
        tokens_per_second=tokens_per_second,
        timestamp=datetime.now().isoformat(),
    )


@app.get("/stats")
async def get_stats():
    """서버 통계를 반환합니다."""
    uptime = time.time() - server_start_time

    stats = {
        "uptime_seconds": uptime,
        "uptime_hours": uptime / 3600,
        "model_loaded": llm_engine is not None,
        "stt_loaded": stt_processor is not None,
        "timestamp": datetime.now().isoformat(),
    }

    if llm_engine:
        stats.update(
            {
                "model_name": get_model_config()["model_name"],
                "gpu_memory_utilization": get_model_config()["gpu_memory_utilization"],
                "max_model_len": get_model_config()["max_model_len"],
            }
        )

    return stats


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "Llama Function Call API (Baseline)",
        "version": "1.0.0",
        "model": get_model_config()["model_name"],
        "endpoints": {
            "POST /predict": "단일 텍스트 쿼리 예측",
            "POST /predict_audio": "오디오 파일 예측 (STT + LLM)",
            "GET /stats": "서버 통계",
            "GET /docs": "FastAPI 문서 (Swagger UI)",
        },
    }


def parse_args():
    """명령행 인자 파싱"""
    parser = argparse.ArgumentParser(description="vLLM Llama Function Call API 서버")
    parser.add_argument(
        "--model_name",
        type=str,
        default="./references/llama_function_call_merged",
        help="모델 이름 혹은 경로",
    )
    parser.add_argument("--host", type=str, default="0.0.0.0", help="서버 호스트")
    parser.add_argument("--port", type=int, default=8000, help="서버 포트")
    parser.add_argument("--workers", type=int, default=1, help="워커 수")
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.5, help="GPU 메모리 사용률")
    parser.add_argument("--max_model_len", type=int, default=150, help="최대 모델 길이")
    parser.add_argument("--tensor_parallel_size", type=int, default=1, help="텐서 병렬 크기")
    parser.add_argument(
        "--log_level", type=str, default="ERROR", choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="로그 레벨"
    )
    parser.add_argument("--max_num_batched_tokens", type=int, default=150, help="배치 최대 토큰 수")
    parser.add_argument("--max_num_seqs", type=int, default=1, help="배치 최대 시퀀스 수")
    parser.add_argument("--kv_cache_dtype", type=str, default="fp8_e5m2", help="KV 캐시 데이터 타입")
    parser.add_argument("--disable_enforce_eager", action="store_true", help="연산 즉시 실행 비활성화")

    return parser.parse_args()


def main():
    load_dotenv(override=True)
    """메인 함수"""
    args = parse_args()
    os.environ["VLLM_MODEL_NAME"] = args.model_name
    os.environ["VLLM_GPU_MEMORY_UTILIZATION"] = str(args.gpu_memory_utilization)
    os.environ["VLLM_MAX_MODEL_LEN"] = str(args.max_model_len)
    os.environ["VLLM_TENSOR_PARALLEL_SIZE"] = str(args.tensor_parallel_size)
    os.environ["VLLM_MAX_NUM_BATCHED_TOKENS"] = str(args.max_num_batched_tokens)
    os.environ["VLLM_MAX_NUM_SEQS"] = str(args.max_num_seqs)
    os.environ["VLLM_KV_CACHE_DTYPE"] = args.kv_cache_dtype
    os.environ["VLLM_ENFORCE_EAGER"] = str(not args.disable_enforce_eager)

    logging.getLogger().setLevel(getattr(logging, args.log_level))

    logger.info(f"vLLM API 서버 시작 중...")
    logger.info(f"모델 이름: {args.model_name}")
    logger.info(f"서버 주소: {args.host}:{args.port}")

    uvicorn.run(
        "vllm_api_server:app",
        host=args.host,
        port=args.port,
        workers=args.workers,
        log_level=args.log_level.lower(),
        reload=False,
    )


if __name__ == "__main__":
    main()
