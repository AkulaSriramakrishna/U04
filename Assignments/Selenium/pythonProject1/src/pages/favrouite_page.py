from selenium.webdriver.common.by import By
from src.pages.locators import locators

class Favourites(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.Favourites_button = driver.find_element(By.ID,locators.favourites_button)

    def click_favourite(self):
        return self.Favourites_button