from dataclasses import dataclass

from PIL.Image import Image

@dataclass(slots=True)
class FeatureDocument:
    image: Image

    words: list[str]

    boxes: list[list[int]]

    labels: list[str]