import pytest
from .pages.product_offer_page import ProductOfferPage

@pytest.mark.parametrize('offer',
                             ["offer0", "offer1", "offer2", "offer3",
                              "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])


def test_guest_can_add_product_with_offer_to_basket(browser, offer):
    product_page = ProductOfferPage(browser, offer)
    product_page.open()
    book_title = product_page.get_title()
    price = product_page.get_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_in_basket(book_title)
    product_page.should_be_correct_price(price)
