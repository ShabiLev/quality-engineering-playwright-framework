from __future__ import annotations

from playwright.sync_api import expect
from .base_page import BasePage


class ExamplePage(BasePage):
    @property
    def heading(self):
        return self.page.get_by_role("heading", level=1)

    @property
    def details_link(self):
        return self.page.get_by_role("link", name="View synthetic details")

    def assert_loaded(self) -> None:
        expect(self.heading).to_have_text("Quality Engineering Demo")
        expect(self.details_link).to_be_visible()
        expect(self.details_link).to_have_attribute("href", "details.html")
