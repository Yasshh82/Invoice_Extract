from pathlib import Path


class SROIELabelParser:

    def parse(self, label_file: Path):

        entities = []

        with open(label_file, encoding="utf-8") as f:

            for line in f:
                line = line.strip()
                if not line:
                    continue

                key, value = line.split(",", 1)

                entities.append({
                    "label": key.strip().upper(),
                    "value": value.strip()
                })

        return entities