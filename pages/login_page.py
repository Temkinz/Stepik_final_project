from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_REG = (By.CSS_SELECTOR, "input#id_registration-email")
    INPUT_PASSWORD_REG = (By.CSS_SELECTOR, "input#id_registration-password1")
    INPUT_PASSWORD_REG_REPEAT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name = 'registration_submit']")

    INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, "input#id_login-username")
    INPUT_PASSWORD_LOGIN = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name = 'login_submit']")

    login_email = "test30082020@gmail.com"
    login_password = "Test202020"

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

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        self.is_element_present_new(*self.LOGIN_FORM)
        assert True, "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present_new(*self.REGISTER_FORM)
        assert True, "Register form is not presented"

    def login_form_is_present(self):
        self.is_element_present_new(*self.LOGIN_FORM)
