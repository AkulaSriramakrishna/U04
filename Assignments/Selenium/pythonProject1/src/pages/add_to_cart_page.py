from selenium.webdriver.common.by import By
from src.pages.locators import locators


class Add_to_cart(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.Add_to_cart = driver.find_element(By.XPATH, locators.add_to_cart)
        self.Sort = driver.find_element(By.XPATH, locators.apple_sort_checkbox)
        self.Checkout = driver.find_element(By.XPATH, locators.checkout_button)

    def click_add_to_cart(self):
        return self.Add_to_cart

    def click_apple_sort(self):
        return self.Sort

    def click_checkout(self):
        return self.Checkout
