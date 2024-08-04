from time import sleep
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config
from src.pages.more_page import MorePage


class TestPacketPublishing(Web_driver_setup):
    def test_packet_publishing(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_packet_publishing()
            sleep(10)
        except:
            assert 1 == 0, 'something went wrong'

    def test_find_my_candy(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_find_my_candy()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_automation_sandbox(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_automation_sandbox()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

    def test_graveyard_golfing(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_graveyard_golfing()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


    def test_magic_object_model(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_magic_object_model()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


    def test_sandbox_tool(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_sandbox_page()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


    def test_vampire_blog(self):
        try:
            driver = self.driver
            driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            sleep(5)
            page = MorePage(driver)
            page.get_more_menu()
            sleep(5)
            page.click_vampire_blog()
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'

