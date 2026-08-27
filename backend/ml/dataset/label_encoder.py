import json

from pathlib import Path


class LabelEncoder:
    def __init__(self):
        self.label_to_id = {"O": 0}
        self.id_to_label = {0: "O"}

    def fit(self, documents):
        entity_types = set()

        for document in documents:

            for entity in document["entities"]:
                entity_types.add(entity["label"].upper())

        index = 1

        for entity in sorted(entity_types):
            for prefix in ("B", "I"):
                label = f"{prefix}-{entity}"

                self.label_to_id[label] = index
                self.id_to_label[index] = label

                index += 1

        return self

    def encode(self, label):
        return self.label_to_id[label]

    def decode(self, index):
        return self.id_to_label[index]

    def save(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "label_to_id": self.label_to_id,
                    "id_to_label": {str(k): v for k, v in self.id_to_label.items()}
                },
                file,
                indent=4
            )

    @classmethod
    def load(cls, path: Path):
        with open(path, encoding="utf-8") as file:
            data = json.load(file)

        encoder = cls()

        encoder.label_to_id = data["label_to_id"]
        

        encoder.id_to_label = {int(k): v for k, v in data["id_to_label"].items()}

        return encoder