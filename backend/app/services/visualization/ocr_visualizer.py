from pathlib import Path

from .bbox_drawer import BoundingBoxDrawer


class OCRVisualizer:

    def __init__(self):
        self.drawer = BoundingBoxDrawer()

    def visualize(self, workspace, document):

        outputs = []

        for page in document.pages:
            destination = (workspace.visualization/ f"page_{page.page_number:03}.png")

            self.drawer.draw(page.image_path, page, destination)

            outputs.append(destination)

        return outputs