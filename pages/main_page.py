from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    REGISTRATION_MESSAGE_ACTUAL = (By.CSS_SELECTOR, "div.alert-success > div")
    REGISTRATION_MESSAGE_EXPECTED = "Thanks for registering!"


    def check_registration_message(self):
        registration_message = self.browser.find_element(*self.REGISTRATION_MESSAGE_ACTUAL).text
        assert self.REGISTRATION_MESSAGE_EXPECTED in registration_message, \
            f"expected {self.REGISTRATION_MESSAGE_EXPECTED}, got {registration_message}"
