from ml.dataset.models import Entity
from .diagnostics import AlignmentDiagnostics
from .matcher import WindowMatcher
from .models import MatchResult, AlignmentResult
from .normalization import TextNormalizer


class TokenAligner:

    def __init__(self, threshold=90):
        self.threshold = threshold
        self.matcher = WindowMatcher()
        self.normalizer = TextNormalizer()

    def align(self, words: list[str], entities: list[Entity]) -> AlignmentResult:
        labels = ["O"] * len(words)
        matches: list[MatchResult] = []

        normalized_words = [self.normalizer.normalize(word) for word in words]

        for entity in entities:
            normalized_value = self.normalizer.normalize(entity.value)
            if not normalized_value:
                continue

            target_words = normalized_value.split()
            if not target_words:
                continue

            start, end, score = self._match_window(normalized_words, target_words)
            status = self._classify_score(score)

            matches.append(
                MatchResult(
                    label=entity.label,
                    value=entity.value,
                    start=start,
                    end=end,
                    score=score,
                    status=status,
                )
            )

            if start is not None and end is not None and status in {"matched", "partial"}:
                labels[start] = f"B-{entity.label.upper()}"

                for offset in range(1, end - start):
                    labels[start + offset] = f"I-{entity.label.upper()}"

        matched, partial, unmatched = AlignmentDiagnostics.summarize(matches)

        return AlignmentResult(
            labels=labels,
            matches=matches,
            matched=matched,
            partial=partial,
            unmatched=unmatched,
        )

    def _match_window(self, normalized_words: list[str], target_words: list[str]) -> tuple[int | None, int | None, float]:
        start_end, score = self.matcher.match(normalized_words, " ".join(target_words), self.threshold)

        if start_end is None:
            return None, None, score

        start, end = start_end
        return start, end, score

    def _classify_score(self, score: float) -> str:
        if score >= self.threshold:
            return "matched"

        if self.threshold - 10 <= score < self.threshold:
            return "partial"

        return "unmatched"