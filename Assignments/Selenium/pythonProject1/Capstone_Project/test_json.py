import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as firefox_service
with open("ConfigerationFile.json") as json_file:
    config_data = json.load(json_file)

#current_config = config_data['browsers'][1]

for current_config in config_data['browsers']:
    current_browser = current_config['browser']
    current_searchTerm = current_config['Search_Term']
    current_url = current_config['url']

    driver = None

    if current_browser == 'chrome':
        options = Options()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif current_browser == 'firefox':
        options = Options()
        #driver = webdriver.Firefox(service=firefox_service(geckoDriver().install()), options=options)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print('Firefox is working here')

    driver.get(current_url)
    driver.maximize_window()
    Search_box = driver.find_element(By.NAME, 'q')
    Search_box.send_keys(current_searchTerm)
    Search_box.send_keys(Keys.ENTER)
    sleep(5)
    driver.quit()

