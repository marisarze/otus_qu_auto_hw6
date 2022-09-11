import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage


class RegisterPage(BasePage):
    PAGE_NAME = (By.CSS_SELECTOR, "#content > h1")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_CHECK = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE = (By.CSS_SELECTOR, "input[type='submit']")

    def register_account(self, first_name, last_name, email, phone, password):
        first_name_input = self.element(self.FIRST_NAME_INPUT)
        self._input(first_name_input, first_name)

        last_name_input = self.element(self.LAST_NAME_INPUT)
        self._input(last_name_input, last_name)

        email_input = self.element(self.EMAIL_INPUT)
        self._input(email_input, email)

        phone_input = self.element(self.PHONE_INPUT)
        self._input(phone_input, phone)
        
        password_input = self.element(self.PASSWORD_INPUT)
        self._input(password_input, password)

        password_confirm_input = self.element(self.PASSWORD_CONFIRM_INPUT)
        self._input(password_confirm_input, password)

        privacy_check = self.element(self.PRIVACY_CHECK)
        self.click(privacy_check)

        self.click(self.element(self.CONTINUE))