from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from src.pages.configuration import Registration
from src.pages.signin_page import Login_Page

class CreateAccount(object):

    def __init__(self,driver):
        super().__init__()
        self.driver = driver


    def get_create_account_page(self):
        User_Icon = self.driver.find_element(By.XPATH, Locators.User_icon)
        User_Icon.click()
        Create_Account = self.driver.find_element(By.ID, Locators.create_account_page)
        Create_Account.click()

    def get_create_account(self):
        first_name = self.driver.find_element(By.NAME, Locators.create_ac_frst_name)
        first_name.send_keys(Registration.first_name)
        last_name = self.driver.find_element(By.NAME,Locators.create_ac_lst_name)
        last_name.send_keys(Registration.last_name)
        email = self.driver.find_element(By.NAME,Locators.create_ac_email)
        email.send_keys(Registration.email)
        phno = self.driver.find_element(By.NAME,Locators.create_ac_phoneNo)
        phno.send_keys(Registration.phone_no)
        self.driver.execute_script("window.scrollBy(0,20)")
        sleep(5)

    def click_create_account(self):
        create = self.driver.find_element(By.XPATH,Locators.create_ac_button)
        create.click()

    def get_message(self):
        message = self.driver.find_element(By.XPATH, Locators.page_message).text
        return message

    def get_success_msg(self):
        message = self.driver.find_element(By.XPATH, Locators.create_account_message).text
        return message