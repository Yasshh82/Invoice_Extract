from typing import Tuple


def confidence_color(confidence: float) -> Tuple[int, int, int]:
    """
    OpenCV uses BGR.
    """

    if confidence >= 0.95:
        return (0, 255, 0)

    if confidence >= 0.80:
        return (0, 255, 255)

    return (0, 0, 255)