from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.search_result_page import SearchResultPage
from .pages.utils import Utils


def test_user_cant_see_success_message(browser):
    # Arrange
    login_page = LoginPage(browser)
    login_page.open()
    email = Utils.email()
    password = Utils.passwords()
    login_page.register(email, password)
    product_page = ProductPage(browser)
    product_page.open()
    # Assert
    product_page.should_not_be_success_message()


def test_user_should_see_login_link_on_product_page(browser):
    # Arrange
    login_page = LoginPage(browser)
    login_page.open()
    email = Utils.email()
    password = Utils.passwords()
    login_page.register(email, password)
    product_page = ProductPage(browser)
    product_page.open()
    # Assert
    product_page.should_not_be_login_link()

def test_guest_cant_see_success_message(browser):
    # Arrange
    product_page = ProductPage(browser)
    product_page.open()
    # Assert
    product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # Arrange
    product_page = ProductPage(browser)
    product_page.open()
    # Assert
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    # Arrange
    product_page = ProductPage(browser)
    product_page.open()
    # Act
    product_page.go_to_login_page()
    login_page = LoginPage(browser)
    # Assert
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Arrange
    product_page = ProductPage(browser)
    product_page.open()
    # Act
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser)
    # Assert
    basket_page.should_not_be_products_in_basket()
    basket_page.check_basket_is_empty()

def test_search_from_product_page(browser):
    # Arrange
    product_page = ProductPage(browser)
    product_page.open()
    # Act
    product_page.search()
    search_result_page = SearchResultPage(browser, browser.current_url)
    # Assert
    search_result_page.check_search_result()
