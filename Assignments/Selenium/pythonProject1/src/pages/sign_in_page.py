from selenium.webdriver.common.by import By
from src.pages.locators import locators
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains


class sign_in_page(object):
    'Initializing alla the locatior in constructor'
    def __init__(self, driver):
        super().__init__()
        self.driver=driver
        self.user_name=driver.find_element(By.CSS_SELECTOR, locators.username)
        self.password=driver.find_element(By.CSS_SELECTOR, locators.password)
        self.login_button=driver.find_element(By.ID, locators.login_button)

    'This method return user name feild'
    def select_username(self):
        return self.user_name

    'This method return password feild'
    def select_passwort(self):
        return self.password

    'This method return login button'
    def click_login_button(self):
        return self.login_button

    'This method will perform enter key event'
    def press_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER)
        action.perform()