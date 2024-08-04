from selenium.webdriver.common.by import By
from src.pages.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains


class Login_Page(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def get_user_name(self,usename):
        user_id=self.driver.find_element(By.XPATH, Locators.user_id_input_box)
        user_id.send_keys(usename)

    def get_password(self,Key):
        password = self.driver.find_element(By.XPATH, Locators.password_input_box)
        password.send_keys(Key)
        pass

    def click_signin_button(self):
        signin = self.driver.find_element(By.XPATH, Locators.signin_button)
        signin.click()

    def press_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER)
        action.perform()

    def get_signIn_page(self):
        User_Icon = self.driver.find_element(By.XPATH, Locators.User_icon)
        User_Icon.click()
        Sign_Page = self.driver.find_element(By.ID, Locators.signin_page)
        Sign_Page.click()
        #sleep(10)
        #assert self.driver.current_url == 'https://candymapper.com/m/account', 'Login failed'

    def get_reset_password(self,email_id):
        reset_pwd = self.driver.find_element(By.XPATH, Locators.reset_pwd_link)
        reset_pwd.click()
        email = self.driver.find_element(By.NAME, Locators.create_ac_email)
        email.send_keys(email_id)
        reset_btn = self.driver.find_element(By.XPATH, Locators.reset_pwd_btn)
        reset_btn.click()

    def get_msg(self):
        message = self.driver.find_element(By.XPATH, Locators.page_message).text
        return message