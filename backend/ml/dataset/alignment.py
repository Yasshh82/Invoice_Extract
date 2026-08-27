import re
import unicodedata
from rapidfuzz.fuzz import ratio
from dataclasses import dataclass

def normalize_text(text: str) -> str:

    text = unicodedata.normalize("NFKC", text)

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"[^\w\s]", "", text)

    return text.strip()


def tokenize_text(text: str) -> list[str]:

    normalized = normalize_text(text)

    return normalized.split()


def normalize_ocr_words(words):

    result = []

    for word in words:

        text = word["text"]

        normalized = normalize_text(text)

        if not normalized:
            continue

        result.append(
            {
                **word,
                "normalized_text": normalized,
            }
        )

    return result


def similarity(source: str, target: str) -> float:
    return ratio(source, target)


def find_best_window(words, target_tokens, threshold=75):
    if not target_tokens:
        return None

    target_text = " ".join(target_tokens)

    best = None

    target_length = len(target_tokens)

    for start in range(len(words)):

        for size in range(max(1, target_length - 2), target_length + 3):
            end = start + size

            if end > len(words):
                continue

            window = words[start:end]

            window_text = " ".join(word["normalized_text"] for word in window)

            score = similarity(window_text, target_text)

            if (best is None or score > best["score"]):
                best = {
                    "start": start,
                    "end": end,
                    "score": score,
                }

    if (best is None or best["score"] < threshold):
        return None

    return best



@dataclass
class AlignmentResult:
    entity_label: str
    entity_value: str
    start: int | None
    end: int | None
    score: float
    status: str


class EntityAligner:
    def __init__(self, threshold=75):
        self.threshold = threshold

    def align(self, words, entities):
        words = normalize_ocr_words(words)

        results = []

        occupied = set()

        for entity in entities:
            target_tokens = tokenize_text(entity["value"])

            best = find_best_window(words, target_tokens, self.threshold)

            if best is None:
                results.append(
                    AlignmentResult(
                        entity_label=entity["label"],
                        entity_value=entity["value"],
                        start=None,
                        end=None,
                        score=0,
                        status="unmatched"
                    )
                )
                continue

            indices = range(best["start"], best["end"])

            overlap = (set(indices) & occupied)

            if overlap:
                results.append(
                    AlignmentResult(
                        entity_label=entity["label"],
                        entity_value=entity["value"],
                        start=best["start"],
                        end=best["end"],
                        score=best["score"],
                        status="partially_matched"
                    )
                )
                continue

            occupied.update(indices)

            status = ("matched" if best["score"] >= 90 else "partially_matched")

            results.append(
                AlignmentResult(
                    entity_label=entity["label"],
                    entity_value=entity["value"],
                    start=best["start"],
                    end=best["end"],
                    score=best["score"],
                    status=status
                )
            )

        return words, results