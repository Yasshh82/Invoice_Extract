from transformers import LayoutLMv3Processor

from .bio import LABELS


class LayoutLMProcessor:

    def __init__(self):

        self.processor = (LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False))

        self.label_to_id = {label: index for index, label in enumerate(LABELS)}

    def process(self, feature):

        encoding = self.processor(
            images=feature.image,
            text=feature.words,
            boxes=feature.boxes,
            word_labels=[self.label_to_id[x] for x in feature.labels],
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )

        return encoding