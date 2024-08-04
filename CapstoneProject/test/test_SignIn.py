from time import sleep
from src.pages.signin_page import Login_Page
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config


class TestSignin(Web_driver_setup):

    def test_login(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            Sign_in = Login_Page(driver)

            sleep(5)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            # Now opening signIn page form naviaation bar
            Sign_in.get_signIn_page()
            sleep(5)
            # entering credential and signing in
            Sign_in.get_user_name(Config.username)
            Sign_in.get_password(Config.password)
            Sign_in.click_signin_button()
            sleep(10)
            assert self.driver.current_url == 'https://candymapper.com/m/account', 'Login failed'
            driver.close()
            driver.quit()
        except:
            assert 1==0 , 'Login failed'


    def test_wrong_login(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            Sign_in = Login_Page(driver)

            sleep(5)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            # Now opening signIn page form naviaation bar
            Sign_in.get_signIn_page()
            sleep(5)
            # entering credential and signing in
            Sign_in.get_user_name(Config.username1)
            Sign_in.get_password(Config.password1)
            Sign_in.click_signin_button()
            sleep(10)
            assert driver.current_url == 'https://candymapper.com/m/login?err=FAILED_CONTACT_LOGIN&r=%2Fm%2Faccount&app=website'
            driver.close()
            driver.quit()
        except:
            assert 1 == 0, 'Login failed'
