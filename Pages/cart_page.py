from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_msg_empty(self):
        assert self.is_element_present(*CartPageLocators.IMPTY_BASKET), "No message about empty basket"

    def should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_BASKET), "Basket is not empty"
