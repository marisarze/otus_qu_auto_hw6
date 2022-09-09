import pytest
from conftest import driver, url
from PageObjects.MainPage import MainPage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.AfterRegisterPage import AfterRegisterPage

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


# from selenium import webdriver
# driver1 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url1 = r"http://192.168.0.102:8081"
# test_register_button_in_main_page(driver1, url1)

# from selenium import webdriver
# driver2 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url2 = r"http://192.168.0.102:8081"
# test_registration(driver2, url2)

# from selenium import webdriver
# driver3 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url3 = r"http://192.168.0.102:8081"
# test_related_products(driver3, url3)

# from selenium import webdriver
# driver4 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url4 = r"http://192.168.0.102:8081"
# test_related_products(driver4, url4)

# from selenium import webdriver
# driver5 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url5 = r"http://192.168.0.102:8081"
# test_basket(driver5,url5)

