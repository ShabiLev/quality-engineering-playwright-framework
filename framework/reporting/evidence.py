from __future__ import annotations

from pathlib import Path
from playwright.sync_api import Page


def capture_screenshot(page: Page, test_name: str) -> Path:
    output = Path("test-results")
    output.mkdir(parents=True, exist_ok=True)
    path = output / f"{test_name}.png"
    page.screenshot(path=str(path), full_page=True)
    return path
