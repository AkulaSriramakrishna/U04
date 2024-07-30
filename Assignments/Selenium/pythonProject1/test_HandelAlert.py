from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager


options=Options()
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('http://localhost:63342/pythonProject1/Demo.html?_ijt=nclsq7ejiv0283r22u4re69q97&_ij_reload=RELOAD_ON_SAVE')
driver.set_page_load_timeout(30)
#driver.implicitly_wait(10)
driver.maximize_window()

button = driver.find_elements(By.NAME,'alert')
button.click()
obj=driver.switch_to.alert
msg=obj.text
print ("Alert shows following message: "+ msg )
obj.accept()

print(" Clicked on the OK Button in the Alert Window")
sleep(30)