import json


class DatasetManifest:

    def generate(self, documents, output):

        rows = []

        for doc in documents:

            rows.append({
                "image": str(doc.image),
                "ocr": str(doc.ocr),
                "label": str(doc.label),
            })

        with open(output, "w", encoding="utf8") as file:

            json.dump(rows, file, indent=4)