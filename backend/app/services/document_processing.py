from datetime import date
from decimal import Decimal
from pathlib import Path

from ml.inference.models import StructuredInvoice
from ml.inference.pipeline import InferencePipeline
from ml.preprocessing.artifact import get_model_dir
from ml.preprocessing.feature_builder import FeatureBuilder

from app.core.logging import logger
from app.services.pdf_renderer import PDFRenderer
from app.services.image_preprocessor import ImagePreprocessor
from app.services.ocr.engine import OCREngine
from app.services.ocr.paddle_backend import PaddleOCRBackend
from app.services.ocr_storage import OCRStorage
from app.services.workspace import Workspace
from app.services.visualization.ocr_visualizer import OCRVisualizer


class DocumentProcessingService:
    def __init__(self):
        self.renderer = PDFRenderer()
        self.feature_builder = FeatureBuilder()
        self.inference_pipeline = self._load_inference_pipeline()

    def _load_inference_pipeline(self):
        model_dir = get_model_dir()
        if not model_dir.exists() or not (model_dir / "config.json").exists():
            logger.warning("Inference model artifacts are missing at {}", model_dir)
            return None

        try:
            return InferencePipeline(model_dir)
        except Exception:
            logger.exception("Failed to initialize the inference pipeline")
            return None

    def _parse_date(self, value: str | None):
        if not value:
            return None

        try:
            return date.fromisoformat(value)
        except ValueError:
            return None

    def _parse_total(self, value: str | None):
        if not value:
            return None

        try:
            return Decimal(str(value))
        except Exception:
            return None

    def _extract_value(self, value):
        if isinstance(value, dict):
            return value.get("value")
        return value

    def process(self, invoice):
        pdf = Path(invoice.file_path)
        logger.info("Rendering PDF {}", pdf.name)

        pages = self.renderer.render(pdf_path=str(pdf), invoice_id=invoice.id)
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
                preprocessor.preprocess(page, destination)
            )

        logger.info("{} pages preprocessed.", len(processed_pages))

        backend = PaddleOCRBackend()

        engine = OCREngine(backend)

        ocr_document = engine.process(processed_pages)

        OCRStorage.save(workspace, ocr_document)

        visualizer = OCRVisualizer()
        visualizer.visualize(workspace, ocr_document)

        logger.info("OCR finished.")

        feature = self.feature_builder.build_for_inference(ocr_document)

        if self.inference_pipeline is None:
            inference_result = StructuredInvoice(
                vendor_name=None,
                invoice_number=None,
                invoice_date=None,
                gst_number=None,
                total_amount=None,
            )
        else:
            inference_result = self.inference_pipeline.run(feature)

        invoice.vendor_name = self._extract_value(inference_result.vendor_name)
        invoice.invoice_number = self._extract_value(inference_result.invoice_number)
        invoice.invoice_date = self._parse_date(self._extract_value(inference_result.invoice_date))
        invoice.gst_number = self._extract_value(inference_result.gst_number)
        invoice.total_amount = self._parse_total(self._extract_value(inference_result.total_amount))

        return inference_result.to_dict()