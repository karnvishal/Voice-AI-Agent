from openai import OpenAI
from ..utils.config import Config
import os
from pathlib import Path
import tempfile

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def text_to_speech(text, voice="alloy", model="tts-1"):
    """
    Convert text to speech using OpenAI's TTS API
    Returns path to the generated audio file
    """
    try:
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_file:
            speech_file_path = tmp_file.name
        
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        
        response.stream_to_file(speech_file_path)
        
        return speech_file_path
    except Exception as e:
        raise Exception(f"Text-to-speech conversion failed: {str(e)}")