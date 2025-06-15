import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')
    browser.find_element(By.ID, 'alertButton').click()
    time.sleep(1)
    browser.switch_to.alert.accept()

    browser.find_element(By.ID, 'promptButton').click()
    time.sleep(1)
    prompt = browser.switch_to.alert
    prompt.send_keys('Alert')
    prompt.accept()

    browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)
    print(browser.find_element(By.ID, 'secretKey').text)
    time.sleep(5)




# from selenium.webdriver import Chrome
# import time
#
# URL = "https://parsinger.ru/selenium/8/8.3.1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     alert_button = driver.find_element("id", "alertButton").click()
#     alert = driver.switch_to.alert
#     alert.accept()
#     prompt_button = driver.find_element("id", "promptButton").click()
#     prompt = driver.switch_to.alert
#     prompt.send_keys("Alert")
#     prompt.accept()
#     confirm_button = driver.find_element("id", "confirmButton").click()
#     driver.switch_to.alert.accept()
#     time.sleep(1)
#     result = driver.find_element("id", "secretKey").text
#     print(result)
