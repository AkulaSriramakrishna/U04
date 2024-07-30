from time import sleep
from src.pages.log_out_page import log_out
from src.pages.check_out_page import Check_out
from src.pages.sign_in_page import sign_in_page
from src.test_base.web_driver_setup import web_driver_setup
from src.pages.add_to_cart_page import Add_to_cart
from test.Configuration import Config,User_Data
from src.pages.order_success_page import Order_Success

class TestOrdersPlacing(web_driver_setup):
    def test_order_placing(self):
        driver = self.driver
        self.driver.get(Config.url)

        '-----This block is for signin up-----------------'
        sign_in = sign_in_page(driver)
        sign_in.select_username().send_keys(Config.username)
        sign_in.press_enter_key()
        sign_in.select_passwort().send_keys(Config.password)
        sign_in.press_enter_key()
        sign_in.click_login_button().click()
        sleep(5)

        '-----This block is to sort for apple products----'
        sort = Add_to_cart(driver)
        sort.click_apple_sort().click()
        sleep(5)

        '----------This will add product to cart----------'
        sort.click_add_to_cart().click()
        sleep(5)
        '-----------This will take to checkout page-------'
        sort.click_checkout().click()
        sleep(5)

        '-------------This will fill address and place the order---'
        final_checkout = Check_out(driver)
        final_checkout.send_first_name().send_keys(User_Data.first_name)
        final_checkout.send_last_name().send_keys(User_Data.last_name)
        final_checkout.send_address().send_keys(User_Data.address)
        final_checkout.send_state().send_keys(User_Data.state)
        final_checkout.send_pin_code().send_keys(User_Data.pin_code)
        sleep(5)
        final_checkout.click_submit().click()
        sleep(5)
        Success_Message = Order_Success(driver)
        message = Success_Message.send_success_message().text
        print(message)
        sleep(10)
        driver.close()
        driver.quit()
