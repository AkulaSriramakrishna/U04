from selenium.webdriver.common.by import By
from src.pages.locators import Locators

class HalloweenParty(object):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver

    def get_halloween_party(self):
        page = self.driver.find_element(By.XPATH, Locators.halloween_party_page)
        page.click()

    def host_party(self):
        host_party = self.driver.find_element(By.XPATH, Locators.hosting_party)
        host_party.click()

    def host_theme_zombie(self):
        theme = self.driver.find_element(By.XPATH, Locators.host_theme_zombe)
        theme.click()

    def host_theme_ghost(self):
        theme = self.driver.find_element(By.XPATH, Locators.host_theme_ghost)
        theme.click()

    def attend_halloween_party(self):
        attend_party = self.driver.find_element(By.XPATH, Locators.attend_party)
        attend_party.click()

    def attend_theme_zombiteon(self):
        theme = self.driver.find_element(By.XPATH, Locators.zombitiens)
        theme.click()

    def attend_theme_ghostvilla(self):
        theme = self.driver.find_element(By.XPATH, Locators.ghostvilla)
        theme.click()

    def go_back(self):
        theme = self.driver.find_element(By.XPATH, Locators.go_back)
        theme.click()