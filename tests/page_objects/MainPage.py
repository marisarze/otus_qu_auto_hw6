from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    def click_featured_product(self, index):
        """Так делать не нужно! :)"""
        feature_product = self.elements(self.FEATURED_PRODUCT)[index]
        product_name = feature_product.find_element(*self.PRODUCT_NAME).text
        self.click(feature_product)
        return product_name
