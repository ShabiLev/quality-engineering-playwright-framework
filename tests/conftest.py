from __future__ import annotations

import pytest
from framework.config import load_config


@pytest.fixture(scope="session")
def test_config():
    return load_config()


@pytest.fixture(autouse=True)
def configure_page(page, test_config):
    page.set_default_timeout(test_config.default_timeout_ms)
    page.set_viewport_size({
        "width": test_config.viewport_width,
        "height": test_config.viewport_height,
    })
