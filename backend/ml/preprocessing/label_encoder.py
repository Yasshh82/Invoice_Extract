import json
from pathlib import Path


class LabelEncoder:

    def __init__(self):

        self.label_to_id = {"O": 0}
        self.id_to_label = {0: "O"}

    @classmethod
    def load(cls, path: Path | str):
        path = Path(path)

        with open(path, encoding="utf8") as file:
            data = json.load(file)

        encoder = cls()
        encoder.label_to_id = data["label_to_id"]
        encoder.id_to_label = {int(k): v for k, v in data["id_to_label"].items()}

        return encoder

    def fit(self, documents):

        entity_types = set()

        for document in documents:
            for entity in document.entities:
                entity_types.add(entity.label.upper())

        index = 1

        for entity in sorted(entity_types):
            self.label_to_id[f"B-{entity}"] = index
            self.id_to_label[index] = f"B-{entity}"

            index += 1

            self.label_to_id[f"I-{entity}"] = index
            self.id_to_label[index] = f"I-{entity}"

            index += 1

        return self

    def encode(self, label: str) -> int:

        return self.label_to_id[label]

    def decode(self, index: int) -> str:

        return self.id_to_label[index]

    def save(self, output: Path | str):
        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, "w", encoding="utf8") as file:
            json.dump(
                {
                    "label_to_id": self.label_to_id,
                    "id_to_label": {str(k): v for k, v in self.id_to_label.items()},
                },
                file,
                indent=4,
            )