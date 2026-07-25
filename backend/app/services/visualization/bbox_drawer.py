from pathlib import Path
import cv2
import numpy as np

from .colors import confidence_color

class BoundingBoxDrawer:

    def draw(self, image_path: Path, page, output_path: Path):

        image = cv2.imread(str(image_path))

        for word in page.words:
            points = word.bbox

            color = confidence_color(word.confidence)

            polygon = np.array(word.bbox, dtype=np.int32)

            cv2.polylines(image, [polygon], True, color, 2)

            x = int(points[0][0])

            y = int(points[0][1]) - 5

            cv2.putText(image, word.text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        cv2.imwrite(str(output_path), image)