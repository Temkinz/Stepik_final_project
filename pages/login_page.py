from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    INPUT_EMAIL_REG = (By.CSS_SELECTOR, "input#id_registration-email")
    INPUT_PASSWORD_REG = (By.CSS_SELECTOR, "input#id_registration-password1")
    INPUT_PASSWORD_REG_REPEAT = (By.CSS_SELECTOR, "input#id_registration-password2")
    INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, "input#id_login-username")
    INPUT_PASSWORD_LOGIN = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_ALERT = (By.CSS_SELECTOR, "#login_form >  div:nth-child(3) > strong")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name = 'login_submit']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name = 'registration_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    login_email = "test30082020@gmail.com"
    invalid_login_email = "test30082020@gmail.ru"
    login_password = "Test202020"
    login_alert_expected = "Oops! We found some errors"

    login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def __init__(self, browser):
        BasePage.__init__(self, browser, self.login_page_link)

    def register(self, email, password):
        input_email = self.browser.find_element(*self.INPUT_EMAIL_REG)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD_REG)
        input_password.send_keys(password)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD_REG_REPEAT)
        input_password.send_keys(password)
        self.browser.find_element(*self.REGISTRATION_BUTTON).click()

    def login(self):
        input_email = self.browser.find_element(*self.INPUT_EMAIL_LOGIN)
        input_email.send_keys(self.login_email)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD_LOGIN)
        input_password.send_keys(self.login_password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def login_random(self, email, password):
        input_email = self.browser.find_element(*self.INPUT_EMAIL_LOGIN)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD_LOGIN)
        input_password.send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        self.element_is_present(*self.LOGIN_FORM)
        assert True, "Login form is not presented"

    def should_be_register_form(self):
        self.element_is_present(*self.REGISTER_FORM)
        assert True, "Register form is not presented"

    def login_form_is_present(self):
        self.element_is_present(*self.LOGIN_FORM)

    def check_alert_login(self):
        login_alert_actual = self.browser.find_element(*self.LOGIN_ALERT).text
        assert self.login_alert_expected == login_alert_actual, f"{self.login_alert_expected} expected," \
                                                                f"got {login_alert_actual}"

    def login_page_isnt_changed(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.title_contains("Login or register"))
        except TimeoutException:
            return True
        return False

    def check_login_page_doesnt_change(self):
        assert self.login_page_isnt_changed() is True
