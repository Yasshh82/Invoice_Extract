from ml.dataset.models import Entity


class TokenAligner:

    def align(self, words: list[str], entities: list[Entity]) -> list[str]:
        labels = ["O"] * len(words)

        for entity in entities:
            entity_tokens = entity.value.split()
            size = len(entity_tokens)

            for index in range(len(words) - size + 1):
                if words[index:index + size] == entity_tokens:
                    labels[index] = f"B-{entity.label.upper()}"

                    for offset in range(1, size):
                        labels[index + offset] = f"I-{entity.label.upper()}"

                    break

        return labels