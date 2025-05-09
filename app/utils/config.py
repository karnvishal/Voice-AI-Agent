import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WHISPER_MODEL = os.getenv('WHISPER_MODEL', 'base')
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-3.5-turbo')
    TTS_MODEL= os.getenv('TTS_MODEL', 'tts-1') 
    
    VECTORSTORE_PATH = os.getenv('VECTORSTORE_PATH', './vectorstore')

    AUDIO_UPLOAD_FOLDER = os.getenv('AUDIO_UPLOAD_FOLDER', './uploads')
    AUDIO_OUTPUT_FOLDER = os.getenv('AUDIO_OUTPUT_FOLDER', './static')