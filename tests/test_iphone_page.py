import time
import selenium
from PageObjects.MainPage import MainPage
from PageObjects.ProductPage import ProductPage


def test_product_button_in_main(driver, url):
    driver.get(url=url)
    iphone_ref = MainPage(driver).element(MainPage.IPHONE)
    MainPage(driver).click(iphone_ref)
    product_name = ProductPage(driver).get_product_name()
    assert product_name == "iPhone"


def test_add_to_cart(driver, url):
    driver.get(url=url+'/iphone')
    ProductPage(driver).add_to_cart()
    alert = ProductPage(driver).element(ProductPage.ALERT_ADD_TO_CART_SUCCESS)
    assert "You have added" in alert.text


def test_wish_list(driver, url):
    driver.get(url=url+"/iphone")
    ProductPage(driver).add_to_wish_list()
    alert = ProductPage(driver).element(ProductPage.ALERT_ADD_TO_WISH_UNSUCCESS)
    assert "You must" in alert.text


def test_related_products(driver, url):
    driver.get(url=url+'/iphone')
    related_objects_header = ProductPage(driver).element(ProductPage.RELATED_PRODUCTS_HEAD)
    assert related_objects_header.text == 'Related Products'

    related_product = ProductPage(driver).elements(ProductPage.RELATED_PRODUCT)[0]
    related_product_image_ref = ProductPage(driver).element_in_element(related_product, ProductPage.RELATED_PRODUCT_IMAGE_REF)
    assert related_product_image_ref.get_attribute('href').startswith(url)

    product_image =ProductPage(driver).element_in_element(related_product, ProductPage.RELATED_PRODUCT_IMAGE)
    assert product_image.get_attribute('src').endswith('.jpg')


# from selenium import webdriver
# driver1 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url1 = r"http://192.168.0.102:8081"
# test_product_button_in_main(driver1, url1)

# from selenium import webdriver
# driver2 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url2 = r"http://192.168.0.102:8081"
# test_add_to_cart(driver2, url2)

# from selenium import webdriver
# driver4 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url4 = r"http://192.168.0.102:8081"
# test_wish_list(driver4, url4)

# from selenium import webdriver
# driver3 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url3 = r"http://192.168.0.102:8081"
# test_related_products(driver3, url3)



# from selenium import webdriver
# driver5 = webdriver.Chrome(executable_path=r'C:\Users\marisarze\Downloads\browsers\chromedriver.exe')
# url5 = r"http://192.168.0.102:8081"
# test_basket(driver5,url5)
