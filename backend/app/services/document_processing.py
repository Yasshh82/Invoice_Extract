from pathlib import Path
from app.core.logging import logger
from app.services.pdf_renderer import PDFRenderer

class DocumentProcessingService:
    def __init__(self):
        self.renderer = PDFRenderer()

    def process(self, invoice):
        pdf = Path(invoice.file_path)
        logger.info("Rendering PDF {}", pdf.name)

        pages = self.renderer.render(pdf_path=str(pdf), invoice_id = invoice.id)
        invoice.page_count = len(pages)
        logger.info("{} pages rendered.", len(pages))

        #
        # OpenCV preprocessing
        #

        return pages