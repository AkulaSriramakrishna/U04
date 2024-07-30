from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get('https://www.google.com')

Search_box=driver.find_element(By.NAME,'q')
Search_box.send_keys('Akula Akhil')
sleep(20)
Search_box.send_keys(Keys.ENTER)
sleep(30)