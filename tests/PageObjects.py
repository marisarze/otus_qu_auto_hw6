import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    def element_in_element(self, parent_locator, child_locator: tuple):
        #if isinstance(parent_locator, 
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

class CatalogPage(BasePage):
    REFINE_SEARCH_DIV = (By.CSS_SELECTOR, "#content > h3")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    PRODUCT = (By.CSS_SELECTOR, "#div.product-thumb")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.price-new")
    SHOPPING_CART = (By.CSS_SELECTOR, "#header-cart > div > button")
    TO_CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to Cart']")

    def sort_by_price_high_to_low(self):
        sorting_select = Select(self.element(self.SORT_DROPDOWN))
        sorting_select.select_by_visible_text('Price (High > Low)')
    
    def get_product_price(self, product):
        return float(self.element_in_element(product, self.PRODUCT_PRICE).text.replace(",", "")[1:])

    def get_total(self):
        return float(self.element(self.SHOPPING_CART).text.split("$")[1].replace(",", ""))

    def add_to_cart(self, product):
        to_cart_button = self.element_in_element(product, self.TO_CART_BUTTON)
        self.click(to_cart_button)


class LoginPage(BasePage):
    NEW_CUSTOMER_HEAD = (By.CSS_SELECTOR, "#content > div > div:nth-child(1) > div > h2")
    RETURNING_CUSTOMER_HEAD = (By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > h2")
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_CONFIRM = (By.CSS_SELECTOR, "input['value'='Login']")

    def login(self, email, password):
        email_input = self.element(self.EMAIL_INPUT)
        self._input(email_input, email)
        password_input = self.element(self.PASSWORD_INPUT)
        self._input(password_input, password)
        self.click(self.element(self.LOGIN_CONFIRM))


class AfterLoginPage(BasePage):
    pass

class RegisterPage(BasePage):
    PAGE_NAME = (By.CSS_SELECTOR, "#content > h1")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_CHECK = (By.CSS_SELECTOR, "input['value'='Login']")
    CONTINUE = (By.CSS_SELECTOR, "input['type'='submit']")

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

class AfterRegisterPage(BasePage):
    SUCCESS_NOTE = (By.CSS_SELECTOR, '#content > h1')


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
    IPHONE = (By.LINK_TEXT, "iPhone")
    EMPTY_CART_INFO = (By.XPATH, "//div[contains(text(), 'Your shopping cart is empty!')]")
    CART = (By.CSS_SELECTOR, '#cart > button')
    SLIDE_IMAGE_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SLIDE_IMAGE_PREV = (By.CLASS_NAME, "swiper-button-prev")
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".product-layeout > div.product-thumb > div.image")
    WISH_BUTTON = (By.CSS_SELECTOR, "button['data-original-title'='Add to Wish List']")
    NAVBAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav")
    DESKTOPS = (By.LINK_TEXT, "Desktops")
    ALL_DESKTOPS = (By.LINK_TEXT, "Show All Desktops")
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    LOGIN = (By.LINK_TEXT, "Login")
    REGISTER = (By.LINK_TEXT, "Register")

    DESKTOPS = (By.LINK_TEXT, "Desktops")
    LAPTOPS = (By.LINK_TEXT, "Laptops & Notebooks")
    COMPONENTS = (By.LINK_TEXT, "Components")
    TABLETS = (By.LINK_TEXT, "Tablets")
    SOFTWARE = (By.LINK_TEXT, "Software")
    PHONES = (By.LINK_TEXT, "Phones & PDAs")
    CAMERAS = (By.LINK_TEXT, "Cameras")
    MP3_PLAYERS = (By.LINK_TEXT, "MP3 Players")

    SLIDE_ACTIVE_ELEMENT = (By.CSS_SELECTOR, "div.swiper-wrapper > div.swiper-slide-duplicate-active")


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

    def click_login(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.LOGIN))

    def click_register(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.REGISTER))




class ProductPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content > div > div > h1")
    RELATED_PRODUCTS_HEAD = (By.CSS_SELECTOR, '#content > h3')
    RELATED_PRODUCT = (By.CSS_SELECTOR, '#div.product-thumb')
    RELATED_PRODUCT_IMAGE_REF = (By.CSS_SELECTOR, "div.image > a")
    RELATED_PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.image > a > img")

    def add_to_wish_list(self):
        self.click(self.element(self.WISH_LIST))

    def add_to_comparison(self):
        self.click(self.element(self.COMPARE))

    def add_to_cart(self):
        time.sleep(1.5)  # Page loading problem
        self.click(self.element(self.CART))

    def get_product_name(self):
        self.element(self.PRODUCT_NAME).text


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
    UNSUCCESS_LOGIN = (By.CSS_SELECTOR, "#account-login > div.alert.alert-danger.alert-dismissible")

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
