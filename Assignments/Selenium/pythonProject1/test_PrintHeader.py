from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('https://ultimateqa.com/automation')
driver.set_page_load_timeout(5)
home_page_message = driver.find_element(By.XPATH, "//span[contains(text(),'Automation Practice')]")
sleep(5)
message=home_page_message.text

print(message)
