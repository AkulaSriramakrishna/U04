from selenium.webdriver.common.by import By
from src.pages.locators import locators


class Offers_page(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.Offer_Button = driver.find_element(By.ID, locators.offers_button)

    def click_offers(self):
        return self.Offer_Button
