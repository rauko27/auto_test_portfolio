from .main_page import MainPage
from .login_page import LoginPage
from .locators import MainPageLocators

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