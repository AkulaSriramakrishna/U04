from time import sleep
from src.pages.create_account_page import CreateAccount
from src.pages.pop_up_page import PopUp
from src.test_base.web_driver_setup import Web_driver_setup
from src.pages.configuration import Config


class TestCreateAccount(Web_driver_setup):
    def test_create_account(self):
        try:
            driver = self.driver
            self.driver.get(Config.url)
            # This will close pop-up
            Close_PopUp = PopUp(driver)
            Close_PopUp.click_popUp_close()
            # This will re-direct to signUp page
            account = CreateAccount(driver)
            # This fill registration detais
            account.get_create_account_page()
            sleep(5)
            # Checking for sigUp page opening
            msg = account.get_message()
            assert msg == 'Create Account', 'Failed to load page'
            # This will fill all the requried data
            account.get_create_account()
            sleep(5)
            account.click_create_account()
            sleep(5)
            # Getting success message of account creation
            success_msg = account.get_success_msg()
            assert success_msg == 'Check your email', 'Account creation failed'
            sleep(10)
        except:
            assert 1 == 0, 'Something went wrong'


