from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_cart(self):
        btn_add_to_cart = self.browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        btn_add_to_cart.click()

    # проверка соответсвия названия
    def shoud_be_right_name_in_cart(self):
        name_in_product_page = self.browser.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1').text
        name_in_cart = self.browser.find_element(By.XPATH, '//*[@id="messages"]/div[1]/div/strong').text
        assert name_in_cart == name_in_product_page, 'Name in product page != Name in cart'
    # проверка соответсвия цены
    def shoud_be_right_price_in_cart(self):
        price_in_product_page = self.browser.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').text
        price_in_cart = self.browser.find_element(By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong').text
        assert price_in_cart == price_in_product_page, 'Price in product page != Price in cart'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_two(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
