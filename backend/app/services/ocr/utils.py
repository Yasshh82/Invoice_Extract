from typing import List


def normalize_bbox(
    bbox: List[List[int]], image_width: int, image_height: int) -> list[int]:
    """
    Convert PaddleOCR polygon bbox to
    LayoutLMv3 normalized format (0-1000).
    """

    xs = [point[0] for point in bbox]
    ys = [point[1] for point in bbox]

    x0 = min(xs)
    y0 = min(ys)
    x1 = max(xs)
    y1 = max(ys)

    normalized = [
        int(1000 * x0 / image_width),
        int(1000 * y0 / image_height),
        int(1000 * x1 / image_width),
        int(1000 * y1 / image_height)
    ]

    validate_bbox(normalized)

    return normalized

def validate_bbox(bbox: list[int]):

    if len(bbox) != 4:
        raise ValueError("Bounding box must contain four coordinates.")

    if any(coordinate < 0 for coordinate in bbox):
        raise ValueError("Bounding box coordinates must be non-negative.")

    if any(coordinate > 1000 for coordinate in bbox):
        raise ValueError("Bounding box coordinates must be <= 1000.")