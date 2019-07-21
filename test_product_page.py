from .Pages.locators import MainPageLocators
from .Pages.locators import ProductPageLocators
from .Pages.product_page import ProductPage
from .Pages.login_page import LoginPage
from .Pages.cart_page import CartPage
import time
import pytest


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser):
    # link = link.format(link)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_cart()
    time.sleep(2)
    # prod_page.solve_quiz_and_get_code()
    prod_page.shoud_be_right_name_in_cart()
    prod_page.shoud_be_right_price_in_cart()


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     prod_page = ProductPage(browser, link)
#     prod_page.open()
#     prod_page.add_to_cart()
#     prod_page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     prod_page = ProductPage(browser, link)
#     prod_page.open()
#     prod_page.should_not_be_success_message()
#
# def test_message_disappeared_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     prod_page = ProductPage(browser, link)
#     prod_page.open()
#     prod_page.add_to_cart()
#     prod_page.should_not_be_success_message_two()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page_basket = CartPage(browser, link)
    page_basket.should_be_msg_empty()
    page_basket.should_be_empty()