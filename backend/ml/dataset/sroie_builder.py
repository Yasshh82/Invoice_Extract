import json

from pathlib import Path
from PIL import Image

from .bbox import normalize_bbox
from .sroie_labels import SROIELabelParser
from .sroie_ocr import SROIEOCRParser


class SROIEDocumentBuilder:

    def __init__(self):
        self.ocr_parser = SROIEOCRParser()
        self.label_parser = SROIELabelParser()

    def build(self, image_path: Path, ocr_path: Path, label_path: Path):

        image = Image.open(image_path)

        width, height = image.size

        ocr_words = self.ocr_parser.parse(ocr_path)

        entities = self.label_parser.parse(label_path)
        
        words = []

        for item in ocr_words:
            normalized_bbox = normalize_bbox(item["bbox"], width, height)

            words.append({
                "text": item["text"],
                "bbox": item["bbox"],
                "normalized_bbox": normalized_bbox
            })

        return {
            "image": image_path,
            "width": width,
            "height": height,
            "words": words,
            "entities": entities
        }