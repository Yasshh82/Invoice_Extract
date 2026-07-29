import json
from pathlib import Path

from .models import Entity


class SROIEParser:

    def parse(self, label_file: Path) -> list[Entity]:
        entities = []

        with open(label_file, encoding="utf8") as file:
            content = file.read().strip()

        if not content:
            return entities

        try:
            payload = json.loads(content)
        except json.JSONDecodeError:
            payload = None

        if isinstance(payload, dict):
            for key, value in payload.items():
                entities.append(Entity(label=str(key).strip(), value=str(value).strip()))
            return entities

        for line in content.splitlines():
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            entities.append(Entity(label=key.strip(), value=value.strip()))

        return entities