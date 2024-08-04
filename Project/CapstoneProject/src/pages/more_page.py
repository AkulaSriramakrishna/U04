from selenium.webdriver.common.by import By
from src.pages.locators import Locators


class MorePage(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def get_more_menu(self):
        more = self.driver.find_element(By.XPATH, Locators.more_page)
        more.click()

    def click_packet_publishing(self):
        page = self.driver.find_element(By.XPATH, Locators.packet_publish_page)
        if page.is_displayed():
            page.click()

    def click_find_my_candy(self):
        page = self.driver.find_element(By.XPATH, Locators.find_my_candy_page)
        if page.is_displayed():
            page.click()

    def click_automation_sandbox(self):
        page = self.driver.find_element(By.XPATH, Locators.automation_sandbox_page)
        if page.is_displayed():
            page.click()

    def click_graveyard_golfing(self):
        page = self.driver.find_element(By.XPATH, Locators.graveYard_golfing_page)
        if page.is_displayed():
            page.click()

    def click_magic_object_model(self):
        page = self.driver.find_element(By.XPATH, Locators.magic_object_model_page)
        if page.is_displayed():
            page.click()

    def click_sandbox_page(self):
        page = self.driver.find_element(By.XPATH, Locators.sand_box_tools_page)
        if page.is_displayed():
            page.click()

    def click_vampire_blog(self):
        page = self.driver.find_element(By.XPATH, Locators.vampires_blog_page)
        if page.is_displayed():
            page.click()