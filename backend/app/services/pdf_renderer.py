import shutil
from pathlib import Path
from pdf2image import convert_from_path
from app.core.config import settings

class PDFRenderer:
    def __init__(self):
        self.temp_root = Path(settings.TEMP_DIR)
        self.temp_root.mkdir(exist_ok=True, parents=True,)

    def render(self, pdf_path:str, invoice_id: int,) -> list[Path]:
        output_dir = (self.temp_root/str(invoice_id))

        output_dir.mkdir(exist_ok=True, parents=True,)

        images = convert_from_path(pdf_path, dpi=settings.PDF_RENDER_DPI)

        rendered_pages = []

        for index, image in enumerate(images):
            page_path = (output_dir/f"page_{index + 1:03}.{settings.PDF_IMAGE_FORMAT}")

            image.save(page_path, settings.PDF_IMAGE_FORMAT.upper(),)

            rendered_pages.append(page_path)

        return rendered_pages

    def cleanup_rendered_pages(invoice_id: int,):
        directory = (Path(settings.TEMP_DIR)/str(invoice_id))

        if directory.exists():
            shutil.rmtree(directory)