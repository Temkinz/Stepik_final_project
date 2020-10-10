from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "header span > a")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    SEARCH_TEXT = "Coders at Work"

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.maximize_window()
        self.url = url
        self.browser.implicitly_wait(timeout)

    def element_is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def element_is_present(self, how, what, timeout=2, poll_frequency=0.2):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def element_is_not_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_basket_page(self):
        self.browser.find_element(*self.BASKET_BUTTON).click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()

    def open(self):
        self.browser.get(self.url)

    def search(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(*self.SEARCH_TEXT)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def should_be_authorized_user(self):
        assert self.element_is_present(*self.USER_ICON), "User icon is not presented," \
                                                             " probably unauthorised user"

    def should_be_login_link(self):
        assert self.element_is_present(*self.LOGIN_LINK), "Login link is not presented"

    def should_not_be_login_link(self):
        assert self.element_is_not_present(*self.LOGIN_LINK), \
            "Login link is presented"
