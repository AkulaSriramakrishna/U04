from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import  ChromeDriverManager


options=Options()
sleep(5)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.saucedemo.com")

sleep(50)