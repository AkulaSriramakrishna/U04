
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_uploads(driver):
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
    driver.implicitly_wait(20)
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "/home/rps/PycharmProjects/pythonProject/a.html"))
    radio_button = driver.find_element(By.ID, 'RESULT_RadioButton-7_0')
    # radio_button.click()
    driver.execute_script("arguments[0].click()", radio_button)
    check_box = driver.find_element(By.ID, 'RESULT_CheckBox-8_2')
    # check_box.click()
    driver.execute_script("arguments[0].click()", check_box)
    select_button = driver.find_element(By.ID, 'RESULT_RadioButton-9')
    drop_down = Select(select_button)
    drop_down.select_by_visible_text('Morning')
    time.sleep(10)
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    driver.find_element(By.ID, "file-submit").click()

    # file_name_element = driver.find_element(By.ID, "uploaded-files")
    # file_name = file_name_element.text
    #
    # assert file_name == "a.html"


test_uploads(driver)
#
# time.sleep(30)
# # def find_element_by_xpath_text(param):
# #     driver.find_element(By.XPATH, f"//span[text()='{param}']")
# #
# #
# # result = find_element_by_xpath_text('Alerts1')
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
# # driver.switch_to.frame('frame2')
#
#
# # def find_element_by_id(param):
# #     try:
#         ele = driver.find_elements(By.XPATH, f'//*[@id="{param}"]')
#         return ele
#     except:
#         print('element not found')
#
#
# elements = find_element_by_id('sampleHeading')
#
# if len(elements) > 0:
#     print('pass')
# else:
#     print('fail')
# driver.switch_to.default_content()
#
# elements = find_element_by_id('framesWrapper')
#
# if len(elements) > 0:
#     print('pass')
# else:
#     print('fail')