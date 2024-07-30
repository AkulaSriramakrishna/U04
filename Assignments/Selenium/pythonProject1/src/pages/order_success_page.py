from selenium.webdriver.common.by import By
from src.pages.locators import locators


class Order_Success(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.Success_Message = driver.find_element(By.ID, locators.success_message)

    def send_success_message(self):
        return self.Success_Message
