import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element_in_element(self, parent_locator, child_locator: tuple):
        if isinstance(parent_locator, tuple):
            return self.element(parent_locator).find_element(*child_locator)
        return parent_locator.find_element(*child_locator)
        
    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait element visibility: {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait elements visibility: {locator}")

    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))
    
    def wait(self, method, *args):
        try:
            return WebDriverWait(self.driver, self.timeout).until(method(*args))
        except TimeoutException:
            raise AssertionError(f"Didn't wait: {method.__name__} done")

    def wait_not(self, method, *args):
        try:
            return WebDriverWait(self.driver, self.timeout).until_not(method(*args))
        except TimeoutException:
            raise AssertionError(f"Didn't wait: {method.__name__} done")