from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CartPage(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def click_checkout(self):
        self.click(self.element_in_element(self.BUTTONS, self.CHECKOUT_LINK))
