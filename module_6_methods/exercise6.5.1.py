import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    element = browser.find_element(By.ID, 'target')
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()
    print(browser.find_element(By.ID, 'secret-key').text)
    time.sleep(5)



