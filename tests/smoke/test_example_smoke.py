import pytest
from framework.pages import ExamplePage


@pytest.mark.smoke
def test_example_domain_is_available(page, test_config):
    home = ExamplePage(page, test_config.base_url)
    home.open()
    home.assert_loaded()
