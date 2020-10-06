from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    SEARCH_RESULT = (By.XPATH, "//h3/a[text()='Coders at Work']")

    def check_search_result(self):
        search_result = self.browser.find_element(*self.SEARCH_RESULT)
        search_result = search_result.text
        assert self.SEARCH_TEXT == search_result, f"Expected {self.SEARCH_TEXT}, got {search_result}"
