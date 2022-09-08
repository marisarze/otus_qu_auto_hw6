from re import M
import pytest
import time
import random
from conftest import driver, url
from PageObjects import MainPage, AlertElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_home_button(driver, url):
    driver.get(url=url)
    home_button = MainPage(driver).element(MainPage.HOME_BUTTON)
    print(type(home_button))
    assert home_button.get_attribute('href') == url+'/index.php?route=common/home'


def test_navbar_elements(driver, url):
    driver.get(url=url)
    navbar = MainPage(driver).element(MainPage.NAVBAR)
    desktops_button = MainPage(driver).element_in_element(navbar, MainPage.DESKTOPS)
    assert desktops_button.get_attribute("href")==url+"/desktops"

    laptops_button = MainPage(driver).element_in_element(navbar, MainPage.LAPTOPS)
    assert laptops_button.get_attribute("href")==url+"/laptop-notebook"

    components_button = MainPage(driver).element_in_element(navbar, MainPage.COMPONENTS)
    assert components_button.get_attribute("href")==url+"/component"

    tablets_button = MainPage(driver).element_in_element(navbar, MainPage.TABLETS)
    assert tablets_button.get_attribute("href")==url+"/tablet"

    software_button = MainPage(driver).element_in_element(navbar, MainPage.SOFTWARE)
    assert software_button.get_attribute("href")==url+"/software"

    phone_pda_button = MainPage(driver).element_in_element(navbar, MainPage.PHONES)
    assert phone_pda_button.get_attribute("href")==url+"/smartphone"

    cameras_button = MainPage(driver).element_in_element(navbar, MainPage.CAMERAS)
    assert cameras_button.get_attribute("href")==url+"/camera"

    cameras_button = MainPage(driver).element_in_element(navbar, MainPage.MP3_PLAYERS)
    assert cameras_button.get_attribute("href")==url+"/mp3-players"


def test_slide_button(driver, url):
    driver.get(url=url)
    old_element_id = MainPage(driver).element(MainPage.SLIDE_ACTIVE_ELEMENT)\
        .get_attribute("data-swiper-slide-index")
    MainPage(driver).slide_image_next()
    time.sleep(2)
    new_element_id = MainPage(driver).element(MainPage.SLIDE_ACTIVE_ELEMENT)\
        .get_attribute("data-swiper-slide-index")
    assert old_element_id!=new_element_id


def test_featured_elements(driver, url):
    driver.get(url=url)
    featured_elements = MainPage(driver).elements(MainPage.FEATURED_PRODUCT)
    choice_index = random.randint(0,len(featured_elements)-1)
    MainPage(driver).wish_featured_product(choice_index)
    alert = AlertElement(driver).wish()
    MainPage(driver).wait(EC.element_to_be_clickable, MainPage.PRODUCT_IMAGE)


def test_basket(driver, url):
    driver.get(url=url)
    basket_button = MainPage(driver).element(MainPage.CART)
    MainPage(driver).click(basket_button)
    assert "open" in basket_button.get_attribute('class')


from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
url = r"http://192.168.0.102:8081"
#test_home_button(driver, url)
#test_navbar_elements(driver, url)
#test_slide_button(driver, url)
test_featured_elements(driver, url)

