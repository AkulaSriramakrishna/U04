from time import sleep
from src.pages.signin_page import Login_Page
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.pop_up_page import PopUp
from src.pages.configuration import Config
from src.pages.my_account_page import MyAccount

class TestMyAccount(Web_driver_setup):

    def test_myAccount(self):
        driver = self.driver
        self.driver.get(Config.url)
        Sign_in = Login_Page(driver)

        sleep(5)
        # This will close pop-up
        Close_PopUp = PopUp(driver)
        Close_PopUp.click_popUp_close()
        sleep(5)
        # Now opening signIn page form naviation bar
        Sign_in.get_signIn_page()
        sleep(5)
        # entering credential and signing in
        Sign_in.get_user_name(Config.username)
        Sign_in.get_password(Config.password)
        Sign_in.click_signin_button()
        sleep(5)

        #Now navigating to my account page
        My_Account = MyAccount(driver)
        My_Account.get_myAccount()

        sleep(5)
        driver.close()
        driver.quit()