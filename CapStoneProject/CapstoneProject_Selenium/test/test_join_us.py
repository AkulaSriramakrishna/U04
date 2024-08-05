from time import sleep
from src.pages.signin_page import Login_Page
from src.pages.pop_up_page import PopUp
from src.pages.join_us_page import JoinUs
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config


class TestJoinus(Web_driver_setup):

    def test_join_us_login(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            # Now opening signIn page form navigation bar
            Sign_in = Login_Page(driver)
            Sign_in.get_signIn_page()
            sleep(5)
            # entering credential and signing in
            msg = Sign_in.get_msg()
            assert msg == 'Account sign in', 'Failed to load signin page'
            Sign_in.get_user_name(Config.username)
            Sign_in.get_password(Config.password)
            Sign_in.click_signin_button()
            sleep(5)
            # Now clicking on join us from navigation bar
            join_us = JoinUs(driver)
            join_us.click_join_us()
            # Checking for valid messgae
            success_msg = join_us.login_success_join()
            assert success_msg == 'Account Login'
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_join_us_loggedOut(self):
       try:
           driver = self.driver
           driver.get(Config.url)
           # This will close pop-up
           Close_PopUp = PopUp(driver)
           Close_PopUp.click_popUp_close()
           sleep(5)
           # This will click on joinUs from navigation bar
           join_us = JoinUs(driver)
           join_us.click_join_us()
           sleep(5)
           # Checking for valid messgae
           success_msg = join_us.login_fail_join()
           assert success_msg == 'Account sign in'
           sleep(10)
       except:
           assert 1 == 0, 'Something went wrong'
