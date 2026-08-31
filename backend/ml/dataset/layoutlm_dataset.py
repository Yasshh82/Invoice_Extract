from datasets import Dataset
from PIL import Image
from transformers import LayoutLMv3Processor


class LayoutLMDatasetBuilder:
    def __init__(self, processor: LayoutLMv3Processor, encoder, max_length=512):
        self.processor = processor
        self.encoder = encoder
        self.max_length = max_length

    def process_document(self, document):
        image = Image.open(document["image"]).convert("RGB")
        words = [word["text"] for word in document["words"]]
        boxes = [word["normalized_bbox"] for word in document["words"]]
        labels = [self.encoder.encode(label) for label in document["bio_labels"]]

        encoding = self.processor(
            images=image,
            text=words,
            boxes=boxes,
            word_labels=labels,
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
        )

        return encoding

    def build(self, documents):
        records = []

        for document in documents:
            encoding = self.process_document(document)
            records.append(dict(encoding))

        return Dataset.from_list(records)