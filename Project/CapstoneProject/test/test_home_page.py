from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.home_page import HomePage

class TestHomePage(Web_driver_setup):
    def test_home_page(self):
        try:
            driver = self.driver
            self.driver.get(Config.url)
            Close_PopUp = PopUp(driver)

            # This will close pop-up
            Close_PopUp.click_popUp_close()
            sleep(5)
            home_page = HomePage(driver)
            home_page.get_home_page()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'