import json

from pathlib import Path

class SROIEOCRParser:

    def parse(self, file: Path) -> dict:
        with open(file, encoding="utf-8") as f:
            data = json.load(f)

        words = []

        for item in data:
            if len(item) < 2:
                continue

            bbox = item[0]

            text = item[1]

            words.append({
                "text": text,
                "bbox": bbox
            })

        return {"words": words}