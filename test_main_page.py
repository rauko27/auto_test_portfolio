from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.locators import MainPageLocators
from .Pages.base_page import BasePage
from .Pages.cart_page import CartPage

def test_guest_should_see_login_link(browser):
    link = MainPageLocators.MAIN_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_LINK
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
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
