import pytest
from conftest import driver, url
from exception_wrappers import *
from PageObjects import *


def test_login_button_in_main_page(driver, url):
    driver.get(url=url)
    MainPage(driver).click_login()
    assert driver.current_url == (url+"/index.php?route=account/login")
    


def test_login_page(driver, url):
    driver.get(url=url+'/index.php?route=account/login')
    left_part_head = LoginPage(driver).element(LoginPage.NEW_CUSTOMER_HEAD)
    assert left_part_head.text == 'New Customer'
    right_part_head = LoginPage(driver).element(LoginPage.RETURNING_CUSTOMER_HEAD)
    assert right_part_head.text == 'Returning Customer'

    LoginPage(driver).login(email="arichbird@mail.com", password="quackquack")
    alert = LoginPage.element(AlertElement.UNSUCCESS_LOGIN)
    assert alert.text == 'Warning: No match for E-Mail Address and/or Password.'
