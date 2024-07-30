from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('https://www.irctc.co.in/nget/')
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.maximize_window()

From = driver.find_element(By.XPATH,"//*[@id='origin']")
From.send_keys('Tatanagar')

Detination = driver.find_element(By.XPATH,"//*[@id='destination']")
Detination.send_keys('Sompeta')

sleep(30)