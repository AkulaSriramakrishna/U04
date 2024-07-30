from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com")
sleep(5)
username=driver.find_element(By.ID,'user-name')
username.send_keys("standard_user")
password=driver.find_element(By.ID,'password')
password.send_keys("secret_sauce")
sleep(10)
login_button=driver.find_element(By.ID,'login-button')
login_button.click()
sleep(10)

if 'inventory.html' in driver.current_url:
    print('Login successfulla and passed')
else:
    print('login is un-successfull')
