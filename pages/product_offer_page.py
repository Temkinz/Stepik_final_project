import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .product_page import ProductPage


class ProductOfferPage(ProductPage):

    def __init__(self, browser, offer):
        product_offer_page_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
        BasePage.__init__(self, browser, product_offer_page_link)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
