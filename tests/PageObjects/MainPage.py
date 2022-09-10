import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    HOME_BUTTON = (By.CSS_SELECTOR, '#logo > a')
    IPHONE = (By.LINK_TEXT, "iPhone")
    EMPTY_CART_INFO = (By.XPATH, "//div[contains(text(), 'Your shopping cart is empty!')]")
    CART = (By.CSS_SELECTOR, '#cart > button')
    SLIDE_IMAGE_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SLIDE_IMAGE_PREV = (By.CLASS_NAME, "swiper-button-prev")
    CENTRAL_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".product-layeout > div.product-thumb > div.image")
    WISH_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    NAVBAR = (By.CSS_SELECTOR, "#menu")
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

    PLEASE_LOGIN = (By.XPATH, "//div[contains(text(), 'You must')]")

    SLIDE_ACTIVE_ELEMENT = (By.CSS_SELECTOR, "div.swiper-slide-active")
    CURRENCY_SWITCHER = (By.CSS_SELECTOR, "#form-currency > div > button")
    CURRENCY_INDICATOR = (By.CSS_SELECTOR, "#form-currency > div > button > strong")
    CURRENCY_EURO = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1)")
    CURRENCY_POUND = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2)")
    CURRENCY_DOLLAR = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3)")


    def slide_image_next(self):
        ActionChains(self.driver).move_to_element(self.element(self.CENTRAL_SLIDER)).perform()
        next_button = self.element(self.SLIDE_IMAGE_PREV)
        ActionChains(self.driver).move_to_element(next_button).pause(0.1).click().perform()

    def slide_image_prev(self):
        ActionChains(self.driver).move_to_element(self.element(self.CENTRAL_SLIDER)).perform()
        prev_button = self.element(self.SLIDE_IMAGE_PREV)
        ActionChains(self.driver).move_to_element(prev_button).pause(0.1).click().perform()

    def click_featured_product(self, index):
        feature_product = self.elements(self.FEATURED_PRODUCT)[index]
        self.click(feature_product)

    def wish_featured_product(self, index):
        product = self.elements(self.FEATURED_PRODUCT)[index]
        wish_button = product.find_element(*self.WISH_BUTTON)
        self.click(wish_button)

    def click_login(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.LOGIN))

    def click_register(self):
        self.click(self.element(self.MY_ACCOUNT))
        self.click(self.element(self.REGISTER))
