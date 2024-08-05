from selenium.webdriver.common.by import By
from src.pages.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

class JoinUs(object):

    def __init__(self,driver):
        super().__init__()
        self.driver = driver

    def click_join_us(self):
        join_us_link = self.driver.find_element(By.XPATH, Locators.join_us_page)
        join_us_link.click()

    def login_success_join(self):
        msg = self.driver.find_element(By.XPATH, Locators.joinUs_login_message).text
        return msg

    def login_fail_join(self):
        msg = self.driver.find_element(By.XPATH, Locators.joinUs_logout_message).text
        return msg

