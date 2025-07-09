import pyaudio
import wave
import os

AUDIO_DIR = "audio/"
os.makedirs(AUDIO_DIR, exist_ok=True)

def record_audio(filename="sentence_01.wav", record_seconds=7):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000  # Whisper expects 16kHz input
    CHUNK = 1024

    audio = pyaudio.PyAudio()

    print("🎙️ Recording... Speak now")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("✅ Recording complete.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    output_path = os.path.join(AUDIO_DIR, filename)
    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"📁 Saved to {output_path}")

if __name__ == "__main__":
    record_audio()
