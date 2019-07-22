from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'accounts/login/'
    MAIN_LINK = 'http://selenium1py.pythonanywhere.com/'


class ProductPageLocators(object):
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
    IMPTY_BASKET = (By.ID, 'content_inner')
    PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="basket_formset"]/div/div')