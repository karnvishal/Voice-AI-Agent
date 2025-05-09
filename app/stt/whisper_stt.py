import whisper
from ..utils.config import Config
import os

model = None

def load_model():
    global model
    if model is None:
        model = whisper.load_model(Config.WHISPER_MODEL, device="cpu")
    return model

def transcribe_audio(audio_path):
    """
    Transcribe audio file to text using Whisper
    """
    try:
        model = load_model()
        transcribe_options = {"fp16": False}
        result = model.transcribe(audio_path, **transcribe_options)
        return result["text"]
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}")