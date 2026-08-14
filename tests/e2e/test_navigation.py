import pytest
from playwright.sync_api import expect
from framework.pages import ExamplePage


@pytest.mark.e2e
def test_primary_link_is_actionable(page, test_config):
    home = ExamplePage(page, test_config.base_url)
    home.open()
    link = home.primary_link
    expect(link).to_be_visible()
    href = link.get_attribute("href")
    assert href is not None and href.startswith(("http://", "https://"))
