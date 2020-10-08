from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) div > strong")
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, "div h1")
    BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) div > strong")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")

    product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, self.product_page_link)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.BOOK_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*self.BOOK_MESSAGE), \
            "Success message is disappeared"

    def add_product_to_basket(self):
        self.browser.find_element(*self.PRODUCT_ADD_BUTTON).click()

    def get_title(self):
        book_title = self.browser.find_element(*self.BOOK_TITLE).text
        return book_title

    def get_price(self):
        price = self.browser.find_element(*self.PRICE).text
        return price