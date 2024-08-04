from time import sleep
from src.pages.create_account_page import CreateAccount
from src.pages.signin_page import Login_Page
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config

class TestCreateAccount(Web_driver_setup):
    def test_create_account(self):
        driver = self.driver
        self.driver.get(Config.url)
        Sign_in = Login_Page(driver)

        sleep(5)
        # This will close pop-up
        Close_PopUp = PopUp(driver)
        Close_PopUp.click_popUp_close()

        sleep(10)

        #This will re-direct to signUp page
        account = CreateAccount(driver)
        #This fill registration detais
        account.get_create_account_page()
        sleep(5)
        account.get_create_account()
        sleep(5)
        account.click_create_account()
        sleep(10)