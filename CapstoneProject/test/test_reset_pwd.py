from time import sleep
from src.pages.signin_page import Login_Page
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config, Registration


class TestResetPwd(Web_driver_setup):

    def test_reset_pwd(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            Sign_in = Login_Page(driver)
            Sign_in.get_signIn_page()
            sleep(10)
            Sign_in.get_reset_password(Registration.email)
            sleep(10)
        except:
            assert 1==0, 'Error'

    def test_wrng_reset_pwd(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            Sign_in = Login_Page(driver)
            Sign_in.get_signIn_page()
            sleep(10)
            Sign_in.get_reset_password(Registration.email1)
            sleep(10)
        except:
            assert 1==0, 'Error'