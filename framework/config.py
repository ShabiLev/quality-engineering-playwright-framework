from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import yaml


@dataclass(frozen=True)
class TestConfig:
    base_url: str
    default_timeout_ms: int = 10_000
    viewport_width: int = 1440
    viewport_height: int = 900


def load_config(path: str | Path = "config/demo.yaml") -> TestConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    app = data.get("app", {})
    viewport = data.get("viewport", {})
    return TestConfig(
        base_url=os.getenv("QE_BASE_URL", app.get("base_url", "http://127.0.0.1:8000/demo")),
        default_timeout_ms=int(app.get("default_timeout_ms", 10_000)),
        viewport_width=int(viewport.get("width", 1440)),
        viewport_height=int(viewport.get("height", 900)),
    )
