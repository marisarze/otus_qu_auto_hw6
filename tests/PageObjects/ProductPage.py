import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage


class ProductPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content > div.row > div.col-sm-4 > h1")
    RELATED_PRODUCTS_HEAD = (By.CSS_SELECTOR, '#content > h3')
    RELATED_PRODUCT = (By.CSS_SELECTOR, 'div.product-thumb')
    RELATED_PRODUCT_IMAGE_REF = (By.CSS_SELECTOR, "div.image > a")
    RELATED_PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.image > a > img")
    ALERT_ADD_TO_CART_SUCCESS = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible")
    ALERT_ADD_TO_WISH_UNSUCCESS = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible")
    def add_to_wish_list(self):
        self.click(self.element(self.WISH_LIST))

    def add_to_comparison(self):
        self.click(self.element(self.COMPARE))

    def add_to_cart(self):
        time.sleep(1.5) 
        self.click(self.element(self.CART))

    def get_product_name(self):
        return self.element(self.PRODUCT_NAME).text