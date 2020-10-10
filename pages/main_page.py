from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    SUCCESS_MESSAGE_ACTUAL = (By.CSS_SELECTOR, "div.alert-success > div")
    REGISTER_MESSAGE_EXPECTED = "Thanks for registering!"
    LOGIN_MESSAGE_EXPECTED = "Welcome back"

    main_page_link = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, self.main_page_link)

    def check_registration_message(self):
        registration_message = self.browser.find_element(*self.SUCCESS_MESSAGE_ACTUAL).text
        assert self.REGISTER_MESSAGE_EXPECTED in registration_message, \
            f"expected {self.REGISTER_MESSAGE_EXPECTED}, got {registration_message}"

    def check_login_message(self):
        login_message = self.browser.find_element(*self.SUCCESS_MESSAGE_ACTUAL).text
        assert self.LOGIN_MESSAGE_EXPECTED in login_message, \
            f"expected {self.LOGIN_MESSAGE_EXPECTED}, got {login_message}"
