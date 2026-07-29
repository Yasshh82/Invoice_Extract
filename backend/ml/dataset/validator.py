from pathlib import Path


class DatasetValidator:

    def validate(self, documents):

        for document in documents:

            assert document.image.exists()
            assert document.ocr.exists()
            assert document.label.exists()