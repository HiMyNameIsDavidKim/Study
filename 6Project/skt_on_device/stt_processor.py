import logging
import torch
import librosa
import soundfile as sf
import noisereduce as nr
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

# bitsandbytes 가용성 확인
try:
    import bitsandbytes as bnb
    BITSANDBYTES_AVAILABLE = True
except ImportError:
    BITSANDBYTES_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SenseVoiceSTT:
    def __init__(self,
                 model_id: str = "FunAudioLLM/SenseVoiceSmall",
                 device: str = "cuda",
                 use_half_precision: bool = True,
                 use_8bit: bool = True):
        self.model_id = model_id
        self.device = device if torch.cuda.is_available() else "cpu"
        self.use_half_precision = use_half_precision and torch.cuda.is_available()
        self.use_8bit = use_8bit and BITSANDBYTES_AVAILABLE and torch.cuda.is_available()
        self.model = None
        self._load_model()

    def _load_model(self):
        logger.info(f"Loading SenseVoice STT model: {self.model_id} on device: {self.device}")
        model_kwargs = {
            "model": self.model_id,
            "trust_remote_code": True,
            "device": self.device,
            "vad_model": "fsmn-vad",
            "vad_kwargs": {"max_single_segment_time": 15000},
            "hub": "hf",
            "disable_update": True,
            "max_memory": {0: "0.1GB"},
        }
        if self.use_8bit:
            model_kwargs.update({"load_in_8bit": True, "device_map": "auto"})
        self.model = AutoModel(**model_kwargs)
        if hasattr(self.model, 'eval'):
            self.model.eval()
        if self.use_half_precision and not self.use_8bit:
            if hasattr(self.model, 'half'):
                self.model = self.model.half()
            elif hasattr(self.model, 'model') and hasattr(self.model.model, 'half'):
                self.model.model = self.model.model.half()
        logger.info("SenseVoice STT model loaded successfully.")

    def _denoise_audio(self, audio_path: str, sr: int = 16000) -> str:
        """노이즈 제거 후 임시 파일 반환"""
        y, sr = librosa.load(audio_path, sr=sr)
        reduced = nr.reduce_noise(y=y, sr=sr)
        tmp_path = audio_path.replace(".wav", "_denoised.wav")
        sf.write(tmp_path, reduced, sr)
        return tmp_path

    def transcribe(self, audio_path: str) -> str:
        if not self.model:
            logger.error("STT model is not loaded.")
            return "Error: STT model not loaded."

        logger.info(f"Transcribing audio file (with denoise): {audio_path}")
        try:
            # 노이즈 제거
            clean_path = self._denoise_audio(audio_path)

            with torch.no_grad():
                if self.device == "cuda" and self.use_half_precision:
                    with torch.cuda.amp.autocast():
                        result = self.model.generate(
                            input=clean_path,
                            cache={},
                            language="ko",
                            use_itn=False,
                            hub="hf",
                        )
                else:
                    result = self.model.generate(
                        input=clean_path,
                        cache={},
                        language="ko",
                        use_itn=False,
                        hub="hf",
                    )

            transcribed_text = rich_transcription_postprocess(result[0]["text"])
            logger.info(f"Transcription successful. Result: {transcribed_text}")
            return transcribed_text
        except Exception as e:
            logger.error(f"Failed to transcribe audio: {e}")
            return f"Error: Transcription failed. {e}"