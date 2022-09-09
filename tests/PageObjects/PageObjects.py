import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage      


class AfterLoginPage(BasePage):
    pass


class CartPage(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def click_checkout(self):
        self.click(self.element_in_element(self.BUTTONS, self.CHECKOUT_LINK))


class ComparisonPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    CONTENT = (By.CSS_SELECTOR, "#content")

    def add_to_cart(self):
        self.click(self.element_in_element(self.CONTENT, self.ADD_TO_CART))


class UserPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    WISH_LIST_LINK = (By.LINK_TEXT, 'Wish List')
    PAYMENT_FORM = ((By.ID, "payment-new"))

    def login(self, username, password):
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def open_wish_list(self):
        self.click(self.element(self.WISH_LIST_LINK))
        return self

    def verify_payment_form(self):
        self.element(self.PAYMENT_FORM)
        return self


class AlertElement(BasePage):
    THIS = (By.CSS_SELECTOR, ".alert-success")
    WISH = (By.XPATH, "//div[contains(text(), ' to your wish list!')]")
    COMPARISON = (By.LINK_TEXT, "product comparison")
    LOGIN = (By.LINK_TEXT, "login")
    CART = (By.LINK_TEXT, "shopping cart")
    

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.this = self.element(self.THIS)

    @property
    def comparison(self):
        return self.element(self.COMPARISON)

    @property
    def login(self):
        return self.element(self.LOGIN)

    @property
    def cart(self):
        return self.element(self.CART)

    @property
    def wish(self):
        return self.element(self.WISH)
