from selenium.webdriver.common.by import By
from src.pages.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from src.pages.configuration import Registration


class HomePage(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def get_home_page(self):
        name_input = self.driver.find_element(By.XPATH, Locators.user_name)
        email_input = self.driver.find_element(By.XPATH, Locators.home_email)
        message_input = self.driver.find_element(By.XPATH, Locators.message)
        name_input.send_keys(Registration.first_name)
        email_input.send_keys(Registration.email1)
        message_input.send_keys(Registration.message)
        send_button = self.driver.find_element(By.XPATH, Locators.send_button)
        send_button.click()

    def press_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER)
        action.perform()
