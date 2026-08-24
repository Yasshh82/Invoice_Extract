from pathlib import Path


class SROIEOCRParser:

    def parse(self, file: Path) -> list[dict]:

        words = []

        with open(file, encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) < 9:
                    continue

                coordinates = parts[:8]

                text = ",".join(parts[8:]).strip()

                try:
                    coordinates = [int(value) for value in coordinates]

                except ValueError:
                    continue

                bbox = [
                    [coordinates[0], coordinates[1]],
                    [coordinates[2], coordinates[3]],
                    [coordinates[4], coordinates[5]],
                    [coordinates[6], coordinates[7]],
                ]

                words.append(
                    {
                        "text": text,
                        "bbox": bbox
                    }
                )

        return words