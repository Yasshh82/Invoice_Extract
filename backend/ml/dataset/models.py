from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Entity:
    label: str
    value: str

@dataclass(slots=True)
class TrainingDocument:
    image: Path
    ocr: Path
    label: Path
    entities: list[Entity]