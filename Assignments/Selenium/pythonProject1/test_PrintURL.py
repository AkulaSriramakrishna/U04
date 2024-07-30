from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://tutorialspoint.com')
url = driver.current_url
#driver.set_page_load_timeout(5)
Search_path = driver.find_element(By.XPATH,'//input[@id="search-strings"]')
action = ActionChains(driver)
action.click(on_element=Search_path)
action.send_keys("Python")
action.send_keys(Keys.ENTER)
action.perform()

sleep(30)

