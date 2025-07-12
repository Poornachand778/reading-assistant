from pathlib import Path
from praatio import tgio
import json, difflib

TG_PATH  = Path("mfa_data/output/sentence_01.TextGrid")
REF_TEXT = (
    "Once upon a time, in a dense forest, there lived a fierce lion "
    "who declared himself the king of all animals."
).lower().split()

def load_words(tg_path):
    tg   = tgio.openTextgrid(tg_path)
    tier = tg.tierDict["words"]
    words = [
        {"word": label.lower(), "start": start, "end": end}
        for start, end, label in tier.entryList
        if label.strip()
    ]
    return words

def tag_status(aligned, reference):
    ref_iter = iter(reference)
    current  = next(ref_iter, None)
    for w in aligned:
        if w["word"] == current:
            w["status"] = "correct"
            current     = next(ref_iter, None)
        else:
            ratio  = difflib.SequenceMatcher(None, w["word"], current or "").ratio()
            w["status"] = "approx" if ratio > .6 else "wrong"
    skipped = [current] + list(ref_iter) if current else []
    return aligned, skipped

words, skipped = tag_status(load_words(TG_PATH), REF_TEXT)

out = {
    "reference": " ".join(REF_TEXT),
    "words":     words,
    "skipped_reference_words": skipped,
}

print(json.dumps(out, indent=2))
