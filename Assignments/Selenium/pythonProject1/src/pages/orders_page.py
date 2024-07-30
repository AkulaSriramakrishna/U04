from selenium.webdriver.common.by import By
from src.pages.locators import locators


class orders_page(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.orders_button = driver.find_element(By.ID, locators.orders_button)
        self.add_to_cart = driver.find_element(By.XPATH, locators.add_to_cart)
       # self.check_out = driver.find_element(By.CLASS_NAME, locators.checkout_button)

    def click_orders(self):
        return self.orders_button

    def click_add_to_cart(self):
        return self.add_to_cart

    #def click_checkout(self):
       #return self.check_out
