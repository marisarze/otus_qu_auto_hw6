import pytest
import json
import time
from conftest import driver, url
from selenium.webdriver.common.by import By
from PageObjects.AdminPage import AdminPage


def test_add_new_product(driver, url):
    driver.get(url=url + "/admin")
    secret_path = r'tests/super_secret.json'
    with open(secret_path, 'r') as file:
        secret = json.load(file)
    AdminPage(driver).login(secret['user'], secret['password'])
    AdminPage(driver).open_products()
    old_products_list = AdminPage(driver).elements(AdminPage.PRODUCT_INFO_ROW)
    AdminPage(driver).add_new_product(
        "new awesome product",
        "turbo V4",
        "very fast"
    )
    new_products_list = AdminPage(driver).elements(AdminPage.PRODUCT_INFO_ROW)
    assert len(new_products_list) == len(old_products_list)+1
    new_product_locator = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[14]")
    checkbox = AdminPage(driver).element_in_element(new_product_locator, AdminPage.SELECTED_CHECKBOX)
    AdminPage(driver).click(checkbox)
    delete_button = AdminPage(driver).element(AdminPage.DELETE_BUTTON)
    AdminPage(driver).click(delete_button)
    AdminPage(driver).accept_alert()


def test_remove_product(driver, url):
    driver.get(url=url + "/admin")
    secret_path = r'tests/super_secret.json'
    with open(secret_path, 'r') as file:
        secret = json.load(file)
    AdminPage(driver).login(secret['user'], secret['password'])
    AdminPage(driver).open_products()
    AdminPage(driver).add_new_product(
        "ZZZ new awesome product",
        "turbo V4",
        "very fast"
    )
    old_products_list = AdminPage(driver).elements(AdminPage.PRODUCT_INFO_ROW)
    AdminPage(driver).delete_product(old_products_list[-1])
    new_products_list = AdminPage(driver).elements(AdminPage.PRODUCT_INFO_ROW)
    assert len(new_products_list) == len(old_products_list)-1


def test_add_new_customer(driver, url):
    driver.get(url=url + "/admin")
    secret_path = r'tests/super_secret.json'
    with open(secret_path, 'r') as file:
        secret = json.load(file)
    AdminPage(driver).login(secret['user'], secret['password'])
    AdminPage(driver).add_new_customer(
        first_name="Donald",
        last_name="Duck",
        email="starduck@mail.com",
        phone="123",
        password="quackquack"
    )
    time.sleep(1)
    old_customers = AdminPage(driver).elements(AdminPage.CUSTOMER_ROW)
    AdminPage(driver).add_new_customer(
        first_name="Scrooge",
        last_name="Mcduck",
        email="richbird@mail.com",
        phone="123",
        password="quackquack"
    )
    new_customers = AdminPage(driver).elements(AdminPage.CUSTOMER_ROW)
    assert len(new_customers) == len(old_customers)+1
    AdminPage(driver).delete_all_customers()

