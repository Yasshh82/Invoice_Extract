from pathlib import Path
from PIL import Image
from paddleocr import PaddleOCR

from .base import OCRBackend
from .models import OCRPage, OCRWord
from .sorting import sort_reading_order
from .utils import normalize_bbox

class PaddleOCRBackend(OCRBackend):

    def __init__(self):

        self.model = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)

    def recognize(self, image: Path, page_number: int) -> OCRPage:
        # load image to get its dimensions for bbox normalization
        with Image.open(str(image)) as image_obj:
            width, height = image_obj.size

        result = self.model.predict(str(image))

        words = []

        if result and result[0]:
            for line in result[0]:

                bbox = line[0]
                text = line[1][0]
                confidence = float(line[1][1])

                words.append(
                    OCRWord(text=text, confidence=confidence, bbox=bbox, normalized_bbox=normalize_bbox(bbox, width, height))
                )

        # sort words into reading order
        words = sort_reading_order(words)

        return OCRPage(page_number=page_number, image_path=image, words=words)