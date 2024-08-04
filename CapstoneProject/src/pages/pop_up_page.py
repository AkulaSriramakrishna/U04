from selenium.webdriver.common.by import By
from src.pages.locators import Locators


class PopUp(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_popUp_close(self):
        Close = self.driver.find_element(By.ID, Locators.popUp_close)
        Close.click()
