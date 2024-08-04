from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config

class ClosePopUp(Web_driver_setup):
    def test_closePopUp(self):
        driver = self.driver
        self.driver.get(Config.url)
        Close_PopUp = PopUp(driver)

        # This will close pop-up
        Close_PopUp.click_popUp_close()
        sleep(10)