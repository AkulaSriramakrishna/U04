from selenium.webdriver.common.by import By
from src.pages.locators import locators
class log_out(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.log_out_button = driver.find_element(By.ID, locators.log_out_button)
    def click_logout(self):
        return self.log_out_button
