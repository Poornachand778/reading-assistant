import os
from faster_whisper import WhisperModel

AUDIO_FILE = "audio/sentence_01.wav"
MODEL_SIZE = "base"
TRANSCRIPT_DIR = "transcripts/"
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

def transcribe(audio_path):
    model = WhisperModel(MODEL_SIZE, compute_type="int8")  # or "float16" if GPU supports
    print("🧠 Transcribing...")

    segments, info = model.transcribe(audio_path)
    transcript = ""

    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        transcript += segment.text.strip() + " "

    return transcript.strip()

if __name__ == "__main__":
    if not os.path.exists(AUDIO_FILE):
        raise FileNotFoundError(f"No file at {AUDIO_FILE}")
    
    output_text = transcribe(AUDIO_FILE)

    output_path = os.path.join(TRANSCRIPT_DIR, "sentence_01.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_text)
    
    print(f"✅ Transcription saved to {output_path}")
