from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # The method takes keyword arguments (kwargs)
    def get_locator(self, **kwargs) -> Locator:  # Locator object for interacting with the element
        # Initializes the locator object by inserting dynamic values into the locator.
        locator = self.locator.format(**kwargs)
        # Return the locator object
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
