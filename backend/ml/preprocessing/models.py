from dataclasses import dataclass

from PIL.Image import Image

@dataclass(slots=True)
class FeatureDocument:
    image: Image

    words: list[str]

    boxes: list[list[int]]

    labels: list[str]


@dataclass(slots=True)
class MatchResult:

    label: str

    value: str

    start: int | None

    end: int | None

    score: float

    status: str


@dataclass(slots=True)
class AlignmentResult:

    labels: list[str]

    matches: list[MatchResult]

    matched: int

    partial: int

    unmatched: int