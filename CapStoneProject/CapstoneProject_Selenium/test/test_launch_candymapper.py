from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.launch_candymapper import Launch_Candymapper


class TestLaunchCandymapper(Web_driver_setup):
    def test_launch_candymapper(self):
        try:
            driver = self.driver
            self.driver.get(Config.url)
            closepopup = PopUp(driver)
            closepopup.click_popUp_close()
            sleep(5)

            launch_candymapper = Launch_Candymapper(driver)
            launch_candymapper.click_launch_candymapper()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'
