from time import sleep
from src.pages.signin_page import Login_Page
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.logout_page import Logout


class Testlogout(Web_driver_setup):

    def test_logout(self):
       try:
           driver = self.driver
           self.driver.get(Config.url)
           Sign_in = Login_Page(driver)

           # sleep(5)
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
           # Now logging off
           sign_out = Logout(driver)
           sign_out.click_logout()
           sleep(10)
       except:
           assert 1 == 0, 'Something went wrong'
