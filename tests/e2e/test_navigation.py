import re

import pytest
from playwright.sync_api import expect
from framework.pages import ExamplePage


@pytest.mark.e2e
def test_synthetic_details_navigation(page, test_config):
    home = ExamplePage(page, test_config.base_url)
    home.open()
    home.details_link.click()
    expect(page).to_have_url(re.compile(r"/demo/details\.html$"))
    expect(page.get_by_role("heading", level=1)).to_have_text("Synthetic Details")
