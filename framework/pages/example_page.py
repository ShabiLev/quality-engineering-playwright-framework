from __future__ import annotations

from playwright.sync_api import expect
from .base_page import BasePage


class ExamplePage(BasePage):
    @property
    def heading(self):
        return self.page.get_by_role("heading", level=1)

    def assert_loaded(self) -> None:
        expect(self.heading).to_have_text("Example Domain")
        expect(self.page.get_by_role("link", name="More information...")).to_be_visible()
