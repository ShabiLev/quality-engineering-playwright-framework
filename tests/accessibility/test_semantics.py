import pytest
from playwright.sync_api import expect
from framework.pages import ExamplePage


@pytest.mark.accessibility
def test_primary_semantics_exist(page, test_config):
    home = ExamplePage(page, test_config.base_url)
    home.open()
    expect(page.get_by_role("heading", level=1)).to_be_visible()
    expect(page.get_by_role("link")).to_have_count(1)
