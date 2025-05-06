import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://whoer.net/es'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(5)
    print(browser.find_element(By.CSS_SELECTOR, '.your-ip strong').text)
    time.sleep(5)