from .product_page import ProductPage
from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(ProductPage):
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_EMPTY_TEXT = "Your basket is empty. Continue shopping"
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
    BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) div > strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages p:nth-child(1) > strong")

    basket_page_link = "http://selenium1py.pythonanywhere.com/basket/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, self.basket_page_link)

    def check_basket_is_empty(self):
        basket_message = self.browser.find_element(*self.BASKET_MESSAGE).text
        assert self.BASKET_EMPTY_TEXT in basket_message, f"expected {self.BASKET_EMPTY_TEXT}, got {basket_message}"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*self.PRODUCTS_IN_BASKET), \
            "Product in the basket is presented, but should not be"

    def should_be_product_in_basket(self, book_title):
        book_message = self.browser.find_element(*self.BOOK_MESSAGE).text
        assert book_title == book_message

    def should_be_correct_price(self, price):
        price_message = self.browser.find_element(*self.PRICE_MESSAGE).text
        assert price == price_message
