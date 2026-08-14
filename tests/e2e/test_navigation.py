import pytest
from playwright.sync_api import expect
from framework.pages import ExamplePage


@pytest.mark.e2e
def test_more_information_link_is_actionable(page, test_config):
    home = ExamplePage(page, test_config.base_url)
    home.open()
    link = page.get_by_role("link", name="More information...")
    expect(link).to_have_attribute("href", "https://iana.org/domains/example")
