from selenium.webdriver.common.by import By
from src.pages.locators import Locators


class Launch_Candymapper(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_launch_candymapper(self):
        page = self.driver.find_element(By.XPATH, Locators.launch_candymapper)
        page.click()
