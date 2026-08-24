import json

from pathlib import Path


class SROIELabelParser:

    def parse(self, label_file: Path) -> list[dict]:

        entities = []

        with open(label_file, encoding="utf-8") as file:
            data = json.load(file)

        for label, value in data.items():
            if value is None:
                continue

            value = str(value).strip()

            if not value:
                continue

            entities.append(
                {
                    "label": label.upper(),
                    "value": value
                }
            )

        return entities