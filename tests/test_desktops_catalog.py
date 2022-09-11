import time
import selenium
from PageObjects.MainPage import MainPage
from PageObjects.CatalogPage import CatalogPage


def test_desktop_button(driver, url):

    driver.get(url=url)
    desktop_dropdown = MainPage(driver).element_in_element(MainPage.NAVBAR, MainPage.DESKTOPS)
    MainPage(driver).click(desktop_dropdown)
    all_desktops = MainPage(driver).element(MainPage.ALL_DESKTOPS)
    MainPage(driver).click(all_desktops)
    refine_search = CatalogPage(driver).element(CatalogPage.REFINE_SEARCH_DIV)
    assert refine_search.text == 'Refine Search'


def test_sorting_and_total(driver, url):
    driver.get(url=url+'/desktops')
    CatalogPage(driver).sort_by_price_high_to_low()

    products = CatalogPage(driver).elements(CatalogPage.PRODUCT)
    assert len(products)>0
    price_sum = 0
    price_sum += CatalogPage(driver).get_product_price(products[0])
    CatalogPage(driver).add_to_cart(products[0])
    time.sleep(10)
    price_sum += CatalogPage(driver).get_product_price(products[1])
    CatalogPage(driver).add_to_cart(products[1])
    time.sleep(10)
    total_price = CatalogPage(driver).get_total()
    assert price_sum == total_price

