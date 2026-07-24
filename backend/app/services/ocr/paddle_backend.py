from pathlib import Path

from paddleocr import PaddleOCR

from .base import OCRBackend

from .models import OCRPage
from .models import OCRWord


class PaddleOCRBackend(OCRBackend):

    def __init__(self):

        self.model = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)

    def recognize(self, image: Path, page_number: int) -> OCRPage:

        result = self.model.predict(str(image))

        words = []

        if result and result[0]:
            for line in result[0]:

                bbox = line[0]
                text = line[1][0]
                confidence = float(line[1][1])

                words.append(OCRWord(text=text, confidence=confidence, bbox=bbox))

        return OCRPage(page_number=page_number, image_path=image, words=words)