import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    parent_id = browser.find_element(By.ID, "parent_id")
    child_class = parent_id.find_element(By.CSS_SELECTOR, ".child_class")
    child_class.click()
    password = child_class.get_attribute('password')
    print(password)
    time.sleep(3)