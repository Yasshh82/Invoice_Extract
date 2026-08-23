import json

from pathlib import Path
from PIL import Image

from .bbox import normalize_bbox


class SROIEDocumentBuilder:

    def build(self, image_path: Path, ocr_data: dict):

        image = Image.open(image_path)

        width, height = image.size

        words = []

        for item in ocr_data["words"]:
            text = item["text"]
            bbox = item["bbox"]
            normalized = normalize_bbox(bbox, width, height)

            words.append({
                "text": text,
                "bbox": bbox,
                "normalized_bbox": normalized
            })

        return {
            "image": str(image_path),
            "width": width,
            "height": height,
            "words": words
        }