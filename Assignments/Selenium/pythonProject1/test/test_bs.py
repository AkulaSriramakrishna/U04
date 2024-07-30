from time import sleep
from src.pages.sign_in_page import sign_in_page
from src.pages.home_page import home_page
from src.pages.log_out_page import log_out
from src.pages.orders_page import orders_page
from src.test_base.web_driver_setup import web_driver_setup
from test.Configuration import Config

class TestSignin(web_driver_setup):

    def test_login(self):
        driver = self.driver
        self.driver.get(Config.url)
        sign_in = sign_in_page(driver)
        sign_in.select_username().send_keys(Config.username)
        sign_in.press_enter_key()
        sign_in.select_passwort().send_keys(Config.password)
        sign_in.press_enter_key()
        sign_in.click_login_button().click()
        sleep(5)
        driver.close()
        driver.quit()