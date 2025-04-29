import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.2.1/index.html'
browser = webdriver.Chrome()
browser.get(url)
button = browser.find_element(By.ID, "clickButton")
button.click()
time.sleep(5)
browser.quit()