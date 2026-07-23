from pathlib import Path
import cv2
import numpy as np

class ImagePreprocessor:
    def preprocess(self, image_path: Path, output_path: Path,):

        image = cv2.imread(str(image_path))
        image = self.deskew(image)
        image = self.grayscale(image)
        image = self.denoise(image)
        image = self.enhance(image)
        image = self.threshold(image)

        cv2.imwrite(str(output_path), image)

        return output_path


    def deskew(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        coords = np.column_stack(np.where(gray > 0))

        angle = cv2.minAreaRect(coords)[-1]

        if angle < -45:
            angle = 90 + angle

        else:
            angle = angle

        h, w = image.shape[:2]

        center = (w // 2, h // 2)

        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

        return cv2.warpAffine(image, matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


    def grayscale(self, image):

        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    def denoise(self, image):

        return cv2.fastNlMeansDenoising(image, h=12)


    def enhance(self, image):

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        return clahe.apply(image)


    def threshold(self, image):

        return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 15)