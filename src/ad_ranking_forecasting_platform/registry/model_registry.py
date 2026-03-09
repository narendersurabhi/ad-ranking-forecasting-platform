from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class ModelRecord:
    name: str
    version: str
    stage: str
    artifact_path: str
    metrics: dict
    metadata: dict
    registered_at: str


class LocalModelRegistry:
    def __init__(self, registry_file: Path):
        self.registry_file = registry_file
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.registry_file.exists():
            self.registry_file.write_text("[]")

    def register(self, name: str, version: str, stage: str, artifact_path: str, metrics: dict, metadata: dict):
        records = self.list_records()
        rec = ModelRecord(name, version, stage, artifact_path, metrics, metadata, datetime.now(timezone.utc).isoformat())
        records.append(asdict(rec))
        self.registry_file.write_text(json.dumps(records, indent=2))

    def list_records(self):
        return json.loads(self.registry_file.read_text())
