import logging

from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess

import librosa
import io

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ONNX cuda 테스트
import onnxruntime as ort

print(f"ONNX Runtime 버전: {ort.__version__}")
print(f"사용 가능한 프로바이더: {ort.get_available_providers()}")

if 'CUDAExecutionProvider' in ort.get_available_providers():
    print("✅ CUDA 지원됨")
else:
    print("❌ CUDA 미지원")

# 단독 테스트용
if __name__ == "__main__":
    # SenseVoiceSmall 모델 ONNX
    model_dir = "iic/SenseVoiceSmall"

    model = SenseVoiceSmall(
        model_dir,
        batch_size=1,
        quantize=True,
        device_id="0",
        disable_update=True
    )

    # inference with wav
    # wav_or_scp = ['./train_data_sample/audio/0CMVUL_Level3_B.wav']
    # res = model(wav_or_scp, language="ko", use_itn=False)

    # inference with array
    with open('./train_data_sample/audio/0CMVUL_Level3_B.wav', 'rb') as f:
        audio_bytes = f.read()

    audio_buffer = io.BytesIO(audio_bytes)
    audio_array, sr = librosa.load(audio_buffer, sr=16000, mono=True)

    # (노이즈 전처리 추가)

    res = model(audio_array, language="ko", use_itn=False)
    print(rich_transcription_postprocess(res[0]))
