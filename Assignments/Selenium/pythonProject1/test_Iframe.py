from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('https://demoqa.com/frames')
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame('frame2')


def find_by_id(param):
    ele = driver.find_elements(By.XPATH,f'//*[@id="{param}"]')
    return ele


elements=find_by_id('sampleHeading')
if len(elements) > 0:
    print('Pass')
else:
    print('fail')

driver.switch_to.default_content()


sleep(30)