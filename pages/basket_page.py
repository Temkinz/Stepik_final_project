from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_EMPTY_TEXT = "Your basket is empty. Continue shopping"
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6.h3")


    def check_basket_is_empty(self):
        basket_message = self.browser.find_element(*self.BASKET_MESSAGE).text
        assert self.BASKET_EMPTY_TEXT in basket_message, f"expected {self.BASKET_EMPTY_TEXT}, got {basket_message}"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*self.PRODUCTS_IN_BASKET), \
            "Product in the basket is presented, but should not be"
