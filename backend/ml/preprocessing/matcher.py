from rapidfuzz import fuzz


class WindowMatcher:

    def match(self, words, target, threshold):
        target_words = target.split() if isinstance(target, str) else list(target)

        if not target_words:
            return (None, 0)

        size = len(target_words)
        best = None
        best_score = 0

        for start in range(len(words) - size + 1):
            candidate = " ".join(words[start:start + size])
            score = fuzz.token_sort_ratio(candidate, " ".join(target_words))

            if score > best_score:
                best_score = score
                best = (start, start + size)

        if best and best_score >= threshold:
            return (best, best_score)

        return (None, best_score)