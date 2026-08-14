import pytest
from playwright.sync_api import expect
from framework.pages import ExamplePage


@pytest.mark.ux
@pytest.mark.parametrize("viewport", [(390, 844), (768, 1024), (1440, 900)])
def test_content_remains_visible_across_viewports(page, test_config, viewport):
    page.set_viewport_size({"width": viewport[0], "height": viewport[1]})
    home = ExamplePage(page, test_config.base_url)
    home.open()
    expect(home.heading).to_be_visible()
