from .pages.login_page import LoginPage
from .pages.utils import Utils

def test_unregistered_user_tries_to_login(browser):
    # Arrange
    login_page = LoginPage(browser)
    login_page.open()
    # Act
    login_page.login_form_is_present()
    login_page.login_random(Utils.email(), Utils.password())
    # Assert
    login_page.check_alert_login()
    login_page.check_login_page_doesnt_change()
