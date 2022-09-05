from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ComparisonPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    CONTENT = (By.CSS_SELECTOR, "#content")

    def add_to_cart(self):
        self.click(self.element_in_element(self.CONTENT, self.ADD_TO_CART))
