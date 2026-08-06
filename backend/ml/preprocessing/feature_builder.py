from PIL import Image

from .aligner import TokenAligner
from .models import FeatureDocument

class FeatureBuilder:

    def __init__(self):
        self.aligner = TokenAligner()

    def build(self, document, ocr_document):

        image = Image.open(document.image)

        words = []
        boxes = []
        page_numbers = []

        for page in ocr_document.pages:
            for word in page.words:
                words.append(word.text)
                boxes.append(word.normalized_bbox)
                page_numbers.append(page.page_number)

        alignment = self.aligner.align(words, document.entities)

        return FeatureDocument(image=image, words=words, boxes=boxes, labels=alignment.labels, page_numbers=page_numbers)

    def build_for_inference(self, ocr_document):
        image = None
        words = []
        boxes = []
        page_numbers = []

        for page in ocr_document.pages:
            if image is None:
                image = Image.open(page.image_path)

            for word in page.words:
                words.append(word.text)
                boxes.append(word.normalized_bbox)
                page_numbers.append(page.page_number)

        if image is None:
            raise ValueError("OCR document does not contain any pages")

        return FeatureDocument(image=image, words=words, boxes=boxes, labels=[], page_numbers=page_numbers)

