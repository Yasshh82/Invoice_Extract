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

        for page in ocr_document.pages:
            for word in page.words:

                words.append(word.text)

                boxes.append(word.normalized_bbox)

        alignment = self.aligner.align(words, document.entities)

        return FeatureDocument(image=image, words=words, boxes=boxes, labels=alignment.labels)

