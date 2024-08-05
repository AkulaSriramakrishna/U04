from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.halloween_party_page import HalloweenParty


class TestAddendParty(Web_driver_setup):
    def test_attend_party(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            attend_party = HalloweenParty(driver)
            attend_party.get_halloween_party()
            sleep(5)
            attend_party.attend_halloween_party()
            sleep(10)
        except:
            assert 1==0, 'Something went wrong'


    def test_attend_theme_zombie(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            attend_party = HalloweenParty(driver)
            attend_party.get_halloween_party()
            sleep(5)
            attend_party.attend_halloween_party()
            sleep(5)
            attend_party.attend_theme_zombiteon()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_attend_theme_ghost(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            attend_party = HalloweenParty(driver)
            attend_party.get_halloween_party()
            sleep(5)
            attend_party.attend_halloween_party()
            sleep(5)
            attend_party.attend_theme_ghostvilla()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


    def test_attend_party_goback(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            attend_party = HalloweenParty(driver)
            attend_party.get_halloween_party()
            sleep(5)
            attend_party.attend_halloween_party()
            sleep(5)
            attend_party.go_back()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'