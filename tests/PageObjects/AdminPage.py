import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    CATALOG_LINK = (By.LINK_TEXT, "Catalog")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    PRODUCTS_FORM = (By.CSS_SELECTOR, "#form-product")
    PRODUCT_INFO_ROW = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr")
    SELECTED_CHECKBOX = (By.CSS_SELECTOR, "input[name='selected[]']")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-danger']")

    NEW_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    NEW_PRODUCT_META_TITLE = (By.CSS_SELECTOR, "input[name='product_description[1][meta_title]']")
    NEW_PRODUCT_DATA_TAB = (By.LINK_TEXT, "Data")
    NEW_PRODUCT_MODEL = (By.CSS_SELECTOR, "input[name='model']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    CUSTOMERS_LINK_UPPER = (By.CSS_SELECTOR, "#menu-customer > a")
    CUSTOMERS_LINK_LOWER = (By.CSS_SELECTOR, "#collapse5 > li:nth-child(1) > a")

    NEW_CUSTOMER_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    NEW_CUSTOMER_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    NEW_CUSTOMER_EMAIL = (By.CSS_SELECTOR, "#input-email")
    NEW_CUSTOMER_PHONE = (By.CSS_SELECTOR, "#input-telephone")
    NEW_CUSTOMER_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    NEW_CUSTOMER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    NEW_CUSTOMER_TRACKING_CODE = (By.CSS_SELECTOR, "#input-tracking")
    NEW_CUSTOMER_AFFILATIVE_TAB = (By.CSS_SELECTOR, "#form-customer > ul > li.active > a")
    CUSTOMER_ROW = (By.CSS_SELECTOR, "#form-customer > table > tbody > tr > td:nth-child(1)")

    def login(self, username, password):
        user_input = self.element(self.LOGIN_USERNAME_INPUT)
        self._input(user_input, username)
        password_input = self.element(self.LOGIN_PASSWORD_INPUT)
        self._input(password_input, password)
        submit = self.element(self.LOGIN_SUBMIT_BUTTON)
        self.click(submit)

    def open_products(self):
        catalog_button = self.element(self.CATALOG_LINK)
        self.click(catalog_button)
        products_button = self.element(self.PRODUCTS_LINK)
        self.click(products_button)

    def add_new_product(self, product_name, model, tag_title):
        self.open_products()
        add_new_button = self.element(self.ADD_NEW_BUTTON)
        self.click(add_new_button)
        product_name_input = self.element(self.NEW_PRODUCT_NAME)
        self._input(product_name_input, product_name)
        tag_title_input = self.element(self.NEW_PRODUCT_META_TITLE)
        self._input(tag_title_input, tag_title)
        data_tab = self.element(self.NEW_PRODUCT_DATA_TAB)
        self.click(data_tab)
        model_input = self.element(self.NEW_PRODUCT_MODEL)
        self._input(model_input, model)
        save_button = self.element(self.SAVE_BUTTON)
        self.click(save_button)

    def delete_product(self, product):
        checkbox = self.element_in_element(product, self.SELECTED_CHECKBOX)
        self.click(checkbox)
        delete_button = self.element(self.DELETE_BUTTON)
        self.click(delete_button)
        self.accept_alert()

    def open_customers(self):
        customers_upper_button = self.element(self.CUSTOMERS_LINK_UPPER)
        self.click(customers_upper_button)
        customers_lower_button = self.element(self.CUSTOMERS_LINK_LOWER)
        self.click(customers_lower_button)

    def add_new_customer(self, first_name, last_name, email, phone, password):
        self.open_customers()
        add_new_button = self.element(self.ADD_NEW_BUTTON)
        self.click(add_new_button)

        first_name_input = self.element(self.NEW_CUSTOMER_FIRST_NAME)
        self._input(first_name_input, first_name)
        last_name_input = self.element(self.NEW_CUSTOMER_LAST_NAME)
        self._input(last_name_input, last_name)
        email_input = self.element(self.NEW_CUSTOMER_EMAIL)
        self._input(email_input, email)
        phone_input = self.element(self.NEW_CUSTOMER_PHONE)
        self._input(phone_input, phone)
        password_input = self.element(self.NEW_CUSTOMER_PASSWORD)
        self._input(password_input, password)
        confirm_password_input = self.element(self.NEW_CUSTOMER_CONFIRM_PASSWORD)
        self._input(confirm_password_input, password)
        save_button = self.element(self.SAVE_BUTTON)
        self.click(save_button)

    def delete_customer(self, customer):
        checkbox = self.element_in_element(customer, self.SELECTED_CHECKBOX)
        self.click(checkbox)
        delete_button = self.element(self.DELETE_BUTTON)
        self.click(delete_button)
        self.accept_alert()