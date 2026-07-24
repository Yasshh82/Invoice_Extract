import json


class OCRStorage:

    @staticmethod
    def save(workspace, document):

        output = []

        for page in document.pages:

            words = []

            for word in page.words:
                words.append({"text": word.text, "confidence": word.confidence, "bbox": word.bbox})

            output.append({"page": page.page_number, "words": words})

        with open(workspace.ocr / "ocr.json", "w", encoding="utf8") as f:

            json.dump(output, f, indent=4, ensure_ascii=False)