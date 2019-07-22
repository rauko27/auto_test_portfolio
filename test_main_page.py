import pytest
import time
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.locators import MainPageLocators
from .Pages.base_page import BasePage
from .Pages.cart_page import CartPage
from .Pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_LINK
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_cart()
    page_basket = CartPage(browser, link)
    page_basket.should_be_msg_empty()
    page_basket.should_be_empty()

@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        link = MainPageLocators.LOGIN_URL
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email=email, password='Qwert9876')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(self, browser):
        # link = link.format(link)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.add_to_cart()
        time.sleep(2)
        # prod_page.solve_quiz_and_get_code()
        prod_page.shoud_be_right_name_in_cart()
        prod_page.shoud_be_right_price_in_cart()