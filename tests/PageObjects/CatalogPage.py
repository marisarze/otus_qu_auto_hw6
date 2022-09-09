import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage

class CatalogPage(BasePage):
    REFINE_SEARCH_DIV = (By.CSS_SELECTOR, "#content > h3")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    PRODUCT = (By.CSS_SELECTOR, "div.product-thumb")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price")
    SHOPPING_CART = (By.CSS_SELECTOR, "#cart-total")
    TO_CART_BUTTON = (By.CSS_SELECTOR, "div.button-group > button:nth-child(1)")

    def sort_by_price_high_to_low(self):
        sorting_select = Select(self.element(self.SORT_DROPDOWN))
        sorting_select.select_by_visible_text('Price (High > Low)')
    
    def get_product_price(self, product):
        price_p = self.element_in_element(product, self.PRODUCT_PRICE)
        raw_text = price_p.text.replace(',', '').replace(' ', '')
        price = float(raw_text.split('\n')[0][1:].split('$')[0])
        return price

    def get_total(self):
        return float(self.element(self.SHOPPING_CART).text.split('$')[1].replace(',', '').replace(" ", ""))

    def add_to_cart(self, product):
        to_cart_button = self.element_in_element(product, self.TO_CART_BUTTON)
        self.click(to_cart_button)