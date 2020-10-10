from .product_page import ProductPage
from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(ProductPage):
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
    PRODUCTS_QUANTITY_INPUT = (By.CSS_SELECTOR, "#id_form-0-quantity")
    UPDATE_QUANTITY_BUTTON = (By.CSS_SELECTOR, "div.checkout-quantity button")

    basket_empty_text = "Your basket is empty. Continue shopping"
    basket_page_link = "http://selenium1py.pythonanywhere.com/basket/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, self.basket_page_link)

    def check_basket_is_empty(self):
        basket_message = self.browser.find_element(*self.BASKET_EMPTY_MESSAGE).text
        assert self.basket_empty_text in basket_message, f"expected {self.basket_empty_text}, got {basket_message}"

    def should_not_be_products_in_basket(self):
        assert self.element_is_not_present(*self.PRODUCTS_IN_BASKET), \
            "Product in the basket is presented, but should not be"

    def change_quantity_of_products_to_zero(self):
        quantity_of_products = self.browser.find_element(*self.PRODUCTS_QUANTITY_INPUT)
        quantity_of_products.clear()
        quantity_of_products.send_keys("0")
        self.browser.find_element(*self.UPDATE_QUANTITY_BUTTON).click()


