import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile


recording = []
sample_rate = 16000
is_recording = False

def record_callback(indata,frames, time, status):
    global recording
    if status:
        print(f"⚠️ {status}")
    recording.append(indata.copy())

def start_recording():
    global recording
    recording = []
    print("🎙️ Recording... Press Enter again to stop.")
    stream = sd.InputStream(samplerate=sample_rate, channels=1, callback=record_callback)
    stream.start()
    input()  # Waiting for Enter key to stop
    stream.stop()
    return np.concatenate(recording)

def save_to_wav(audio_data):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        wav.write(tmp_file.name, sample_rate, audio_data)
        return tmp_file.name
