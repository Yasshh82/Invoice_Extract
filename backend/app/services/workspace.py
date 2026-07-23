from pathlib import Path
from app.core.config import settings

class Workspace:
    def __init__(self, invoice_id: int):
        self.root = Path((settings.TEMP_DIR)/str(invoice_id))
        self.rendered = self.root/"rendered"
        self.preprocessed = self.root/"preprocessed"
        self.ocr = self.root/"ocr"
        self.layoutlm = self.root/"layoutlm"
        self.output = self.root/"output"

        for directory in (self.rendered, self.preprocessed, self.ocr, self.layoutlm, self.output):
            directory.mkdir(parents=True, exist_ok=True)