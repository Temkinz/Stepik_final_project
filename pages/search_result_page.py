from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    SEARCH_RESULT = (By.CSS_SELECTOR, "a[title='The shellcoder's handbook']")

    def check_search_result(self):
        search_result = self.browser.find_element(*self.SEARCH_RESULT).text
        assert self.SEARCH_TEXT == search_result, f"Expected {self.SEARCH_TEXT}, got {self.SEARCH_RESULT}"
