import os
import json

STORY_PATH = "data/stories/clever_rabbit.txt"
OUTPUT_JSON = "data/stories/clever_rabbit_sentences.json"

def split_into_sentences(text):
    # Basic sentence split based on punctuation. Can be improved later.
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def load_and_split_story(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Story file not found at {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        story = f.read()
    
    sentences = split_into_sentences(story)
    return sentences

def save_sentences(sentences, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"sentences": sentences}, f, indent=2)

if __name__ == "__main__":
    sentences = load_and_split_story(STORY_PATH)
    save_sentences(sentences, OUTPUT_JSON)
    print(f"✅ Parsed {len(sentences)} sentences.")
