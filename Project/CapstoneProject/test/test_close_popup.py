from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config

class ClosePopUp(Web_driver_setup):
    def test_closePopUp(self):
       try:
           driver = self.driver
           self.driver.get(Config.url)
           # This will close pop-up
           Close_PopUp = PopUp(driver)
           Close_PopUp.click_popUp_close()
       except:
           assert 1 == 0, 'Something went wrong'