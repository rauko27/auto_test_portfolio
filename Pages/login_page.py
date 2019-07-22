from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_in_url = self.browser.current_url
        assert MainPageLocators.LOGIN_URL in login_in_url, "Url link is not True"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register Form is not presented"

    def register_new_user(self, email, password):
        email = self.browser.find_element_by_xpath('//*[@id="id_registration-email"]').send_keys(email)
        password_for_reg = self.browser.find_element_by_xpath('//*[@id="id_registration-password1"]').send_keys(password)
        confirm_password_for_reg = self.browser.find_element_by_xpath('//*[@id="id_registration-password2"]').send_keys(password)
        btn = self.browser.find_element_by_xpath('//*[@id="register_form"]/button').click()