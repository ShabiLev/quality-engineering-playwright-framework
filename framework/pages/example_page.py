from __future__ import annotations

import re
from playwright.sync_api import expect
from .base_page import BasePage


class ExamplePage(BasePage):
    @property
    def heading(self):
        return self.page.get_by_role("heading", level=1)

    @property
    def primary_link(self):
        return self.page.get_by_role("link").first

    def assert_loaded(self) -> None:
        expect(self.heading).to_have_text("Example Domain")
        expect(self.primary_link).to_be_visible()
        expect(self.primary_link).to_have_attribute("href", re.compile(r"^https?://"))
