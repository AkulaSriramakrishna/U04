from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.halloween_party_page import HalloweenParty


class TestHalloweenParty(Web_driver_setup):
    def test_halloween_access(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            Halloween = HalloweenParty(driver)
            Halloween.get_halloween_party()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_hosting_party(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            Halloween = HalloweenParty(driver)
            Halloween.get_halloween_party()
            sleep(5)
            Halloween.host_party()
            sleep(5)
            Halloween.host_theme_zombie()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_theme_zombie(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            Halloween = HalloweenParty(driver)
            Halloween.get_halloween_party()
            sleep(5)
            Halloween.host_party()
            sleep(5)
            Halloween.host_theme_zombie()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


    def test_theme_ghost(self):
       try:
           driver = self.driver
           driver.get(Config.url)
           # This will close pop-up
           Close_PopUp = PopUp(driver)
           Close_PopUp.click_popUp_close()
           sleep(5)
           halloween = HalloweenParty(driver)
           halloween.get_halloween_party()
           sleep(5)
           halloween.host_party()
           sleep(5)
           halloween.host_theme_ghost()
           sleep(10)
       except:
           assert 1 == 0, 'Something went wrong'