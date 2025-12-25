from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # The method takes keyword arguments (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # Locator object for interacting with the element
        # Initializes the locator object by inserting dynamic values into the locator.
        locator = self.locator.format(**kwargs)
        # Return the locator object
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
