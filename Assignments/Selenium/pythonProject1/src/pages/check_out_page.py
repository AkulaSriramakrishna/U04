from selenium.webdriver.common.by import By
from src.pages.locators import locators


class Check_out(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.FirstName = driver.find_element(By.ID, locators.first_name)
        self.LastName = driver.find_element(By.ID, locators.last_name)
        self.Address = driver.find_element(By.ID, locators.address)
        self.State = driver.find_element(By.ID, locators.State_provience)
        self.Pin_Code = driver.find_element(By.ID, locators.pin_code)
        self.Submit_button = driver.find_element(By.ID, locators.submit_button)

    def click_submit(self):
        return self.Submit_button

    def send_first_name(self):
        return self.FirstName

    def send_last_name(self):
        return self.LastName

    def send_address(self):
        return self.Address

    def send_state(self):
        return self.State

    def send_pin_code(self):
        return self.Pin_Code

