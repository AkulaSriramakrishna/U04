from selenium.webdriver.common.by import By
from src.pages.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from src.pages.configuration import Config

class Logout(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_logout(self):
        User_Icon = self.driver.find_element(By.XPATH, Locators.User_icon)
        User_Icon.click()
        logout = self.driver.find_element(By.ID, Locators.logout_button)
        logout.click()