import time
import selenium
from PageObjects.MainPage import MainPage
from PageObjects.LoginPage import LoginPage


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
    alert = LoginPage(driver).element(LoginPage.UNSUCCESS_LOGIN)
    assert alert.text == 'Warning: No match for E-Mail Address and/or Password.'



# from selenium import webdriver
# driver1 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url1 = r"http://192.168.0.102:8081"
# test_login_button_in_main_page(driver1, url1)

# from selenium import webdriver
# driver2 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url2 = r"http://192.168.0.102:8081"
# test_login_page(driver2, url2)

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
