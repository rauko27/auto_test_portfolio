from .Pages.locators import MainPageLocators
from .Pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.shoud_be_right_name_in_cart()
    prod_page.shoud_be_right_price_in_cart()
