import time
import selenium
import random
from PageObjects.MainPage import MainPage


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
    time.sleep(1)
    old_element_id = MainPage(driver).element(MainPage.SLIDE_ACTIVE_ELEMENT)\
        .get_attribute("data-swiper-slide-index")
    MainPage(driver).slide_image_next()
    
    new_element_id = MainPage(driver).element(MainPage.SLIDE_ACTIVE_ELEMENT)\
        .get_attribute("data-swiper-slide-index")
    assert old_element_id!=new_element_id


def test_featured_elements(driver, url):
    driver.get(url=url)
    featured_elements = MainPage(driver).elements(MainPage.FEATURED_PRODUCT)
    choice_index = random.randint(0,len(featured_elements)-1)
    MainPage(driver).wish_featured_product(choice_index)
    alert = MainPage(driver).element(MainPage.PLEASE_LOGIN)
    assert "You must login or" in alert.text 


def test_basket(driver, url):
    driver.get(url=url)
    basket_button = MainPage(driver).element(MainPage.CART)
    MainPage(driver).click(basket_button)
    classes = basket_button.get_attribute('class')
    assert basket_button.get_attribute('aria-expanded')


# from selenium import webdriver
# driver1 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url1 = r"http://192.168.0.102:8081"
# test_home_button(driver1, url1)

# from selenium import webdriver
# driver2 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url2 = r"http://192.168.0.102:8081"
# test_navbar_elements(driver2, url2)

# from selenium import webdriver
# driver3 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url3 = r"http://192.168.0.102:8081"
# test_slide_button(driver3, url3)

# from selenium import webdriver
# driver4 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url4 = r"http://192.168.0.102:8081"
# test_featured_elements(driver4, url4)

# from selenium import webdriver
# driver5 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url5 = r"http://192.168.0.102:8081"
# test_basket(driver5,url5)
