from datasets import Dataset


class LayoutLMDatasetBuilder:
    def __init__(self, processor, encoder):
        self.processor = processor
        self.encoder = encoder

    def build(self, documents):
        records = []

        for document in documents:

            words = [word["text"] for word in document["words"]]

            boxes = [word["normalized_bbox"] for word in document["words"]]

            labels = document["bio_labels"]

            label_ids = [self.encoder.encode(label) for label in labels]

            records.append({
                "image": str(document["image"]),
                "words": words,
                "boxes": boxes,
                "labels": label_ids,
            })

        return Dataset.from_list(records)