import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    NEW_CUSTOMER_HEAD = (By.CSS_SELECTOR, "#content > div > div:nth-child(1) > div > h2")
    RETURNING_CUSTOMER_HEAD = (By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > h2")
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_CONFIRM = (By.CSS_SELECTOR, "input[value='Login']")
    UNSUCCESS_LOGIN = (By.CSS_SELECTOR, "#account-login > div.alert.alert-danger.alert-dismissible")

    def login(self, email, password):
        email_input = self.element(self.EMAIL_INPUT)
        self._input(email_input, email)
        password_input = self.element(self.PASSWORD_INPUT)
        self._input(password_input, password)
        self.click(self.element(self.LOGIN_CONFIRM))