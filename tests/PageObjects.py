import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))
    
    def wait(self, method, *args, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(method(*args))
        except TimeoutException:
            raise AssertionError(f"Didn't wait: {method.__name__} done")

    def wait_not(self, method, *args, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until_not(method(*args))
        except TimeoutException:
            raise AssertionError(f"Didn't wait: {method.__name__} done")


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


class MainPage(BasePage):
    EMPTY_CART_INFO = (By.XPATH, "//div[contains(text(), 'Your shopping cart is empty!')]")
    CART = (By.CSS_SELECTOR, '#cart > button')
    SLIDE_IMAGE_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SLIDE_IMAGE_PREV = (By.CLASS_NAME, "swiper-button-prev")
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".product-layeout > div.product-thumb > div.image")
    WISH_BUTTON = (By.CSS_SELECTOR, "button['data-original-title'='Add to Wish List']")

    def slide_image_next(self):
        next_button = self.element(self.SLIDE_IMAGE_NEXT)
        self.click(next_button)

    def slide_image_prev(self):
        prev_button = self.element(self.SLIDE_IMAGE_PREV)
        self.click(prev_button)

    def click_featured_product(self, index):
        feature_product = self.elements(self.FEATURED_PRODUCT)[index]
        self.click(feature_product)

    def wish_featured_product(self, index):
        wish_button = self.elements(self.FEATURED_PRODUCT)[index].find_element(*self.WISH_BUTTON)
        self.click(wish_button) 



class ProductPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")

    def add_to_wish_list(self):
        self.click(self.element(self.WISH_LIST))

    def add_to_comparison(self):
        self.click(self.element(self.COMPARE))

    def add_to_cart(self):
        time.sleep(1.5)  # Page loading problem
        self.click(self.element(self.CART))


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
