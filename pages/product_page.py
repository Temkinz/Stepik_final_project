
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) div > strong")
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, "div h1")
    BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) div > strong")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.BOOK_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*self.BOOK_MESSAGE), \
            "Success message is disappeared"

    def add_product_to_cart(self):
        self.browser.find_element(*self.PRODUCT_ADD_BUTTON).click()