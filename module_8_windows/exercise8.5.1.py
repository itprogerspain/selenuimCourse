from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for button in buttons:
        button.click()
        time.sleep(0.1)
        browser.switch_to.alert.accept()
        time.sleep(0.1)
        result = browser.find_element(By.ID, 'result').text
        if result:
            print(result)
            break
    # time.sleep(120)

