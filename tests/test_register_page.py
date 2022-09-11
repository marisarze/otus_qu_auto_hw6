import pytest
import json
from conftest import driver, url
from PageObjects.MainPage import MainPage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.AfterRegisterPage import AfterRegisterPage
from PageObjects.AdminPage import AdminPage

def test_register_button_in_main_page(driver, url):
    driver.get(url=url)
    MainPage(driver).click_register()
    assert driver.current_url == url+'/index.php?route=account/register'
    

def test_registration(driver, url):
    driver.get(url=url+'/index.php?route=account/register')
    page_h1_name = RegisterPage(driver).element(RegisterPage.PAGE_NAME)
    assert page_h1_name.text == 'Register Account'
    RegisterPage(driver).register_account(
        first_name="Donald", 
        last_name="Duck",
        email="richbird@mail.com",
        phone="12345678901",
        password="quackquack"
    )
    AfterRegisterPage(driver).element(AfterRegisterPage.SUCCESS_NOTE)
    
    driver.get(url=url + "/admin")
    secret_path = r'tests/super_secret.json'
    with open(secret_path, 'r') as file:
        secret = json.load(file)
    AdminPage(driver).login(secret['user'], secret['password'])
    AdminPage(driver).delete_all_customers()


