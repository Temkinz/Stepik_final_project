from .pages.utils import Utils
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.search_result_page import SearchResultPage


class TestForUserFromMainPage:
    def test_user_can_be_registered(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.login_form_is_present()
        email = Utils.email()
        password = Utils.password()
        login_page.register(email, password)
        main_page = MainPage(browser)
        # Assert
        main_page.check_registration_message()

    def test_user_can_be_logged_in(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.login_form_is_present()
        login_page.login()
        main_page = MainPage(browser)
        # Assert
        main_page.check_login_message()


class TestForGuestFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser)
        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        # Act
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser)
        # Assert
        basket_page.should_not_be_products_in_basket()
        basket_page.check_basket_is_empty()

    def test_search_from_main_page(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        # Act
        main_page.search()
        search_result_page = SearchResultPage(browser, browser.current_url)
        # Assert
        search_result_page.check_search_result()
