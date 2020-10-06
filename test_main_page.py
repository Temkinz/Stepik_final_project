from .pages.utils import Utils
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.search_result_page import SearchResultPage


def test_user_can_be_registered(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    email = Utils.email()
    password = Utils.passwords()
    login_page.register(email, password)
    login_page = MainPage(browser, browser.current_url)
    login_page.check_registration_message()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.check_basket_is_empty()


def test_search_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.search()
    search_result_page = SearchResultPage(browser, browser.current_url)
    search_result_page.check_search_result()
