from app.stt.whisper_stt import transcribe_audio
from app.tts.tts_service import text_to_speech
from app.llm.llm_processor import process_text
from app.rag.retriever import retrieve_context
from app.stt.record_script import start_recording, save_to_wav
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def process_voice():
    try:
        print("🔴 Press Enter to start recording...")
        input()
        audio_data = start_recording()
        print("🛑 Recording stopped.")
        
        wav_path = save_to_wav(audio_data)
        print(f"📁 Saved to: {wav_path}")

        text = transcribe_audio(wav_path)
        print("📝 Transcribed text:", text)

        context = retrieve_context(text)

        processed_text = process_text(text, context)
        audio_output_path = text_to_speech(processed_text)
        print("🔊 Audio output saved at:", audio_output_path)
        print("📎 Exists?", os.path.exists(audio_output_path))

        result= {
            'text_input': text,
            'processed_text': processed_text,
            'audio_output_url': f'/static/{os.path.basename(audio_output_path)}'
        }
        print("📤 Result JSON:")
        print(result)

    except Exception as e:
        return {'error': str(e)}
    finally:
        if 'wav_path' in locals() and os.path.exists(wav_path):
            os.unlink(wav_path)


if __name__ == '__main__':
    process_voice()