from .models import OCRWord


def sort_reading_order(words: list[OCRWord]) -> list[OCRWord]:
    """
    Sort words from top-to-bottom, left-to-right.
    """

    return sorted(words, key=lambda word: (word.normalized_bbox[1], word.normalized_bbox[0]))