import json
import difflib

TRANSCRIPT_PATH = "transcripts/sentence_01.txt"
STORY_PATH = "data/stories/clever_rabbit_sentences.json"
RESULT_PATH = "results/compare_sentence_01.json"

def load_expected_sentence(index=0):
    with open(STORY_PATH, "r", encoding="utf-8") as f:
        story = json.load(f)
    return story["sentences"][index]

def load_transcript():
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def compare_sentences(expected, actual):
    expected_words = expected.lower().split()
    actual_words = actual.lower().split()

    matcher = difflib.SequenceMatcher(None, expected_words, actual_words)
    results = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for i in range(i1, i2):
                results.append({"word": expected_words[i], "status": "correct"})
        elif tag in ('replace', 'delete', 'insert'):
            for i in range(i1, i2):
                if tag in ('replace', 'delete'):
                    results.append({"word": expected_words[i], "status": "missed"})
            for j in range(j1, j2):
                if tag in ('replace', 'insert'):
                    results.append({"word": actual_words[j], "status": "extra"})

    return results

if __name__ == "__main__":
    expected = load_expected_sentence()
    actual = load_transcript()

    print(f"\n📘 Expected: {expected}\n🗣️ Spoken:   {actual}\n")

    alignment = compare_sentences(expected, actual)

    for r in alignment:
        print(f"{r['word']:>12}  →  {r['status']}")

    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "expected": expected,
            "spoken": actual,
            "alignment": alignment
        }, f, indent=2)

    print(f"\n✅ Alignment saved to {RESULT_PATH}")
