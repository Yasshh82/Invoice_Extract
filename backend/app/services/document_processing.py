from pathlib import Path
from app.core.logging import logger
from app.services.pdf_renderer import PDFRenderer
from backend.app.services.image_preprocessor import ImagePreprocessor
from app.services.workspace import Workspace

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

        workspace = Workspace(invoice.id)
        preprocessor = ImagePreprocessor()

        processed_pages = []

        for page in pages:
            destination = workspace.preprocessed / page.name
            processed_pages.append(
                preprocessor.preprocess(
                    page,
                    destination,
                )
            )

        logger.info("{} pages preprocessed.", len(processed_pages))

        return processed_pages