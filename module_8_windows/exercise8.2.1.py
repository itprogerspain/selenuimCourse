import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')
    browser.set_window_size(1200, 720)
    browser.find_element(By.ID, 'checkSizeBtn').click()
    print(browser.find_element(By.ID, 'secret').text)
    time.sleep(5)





# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/selenium/8/8.2.1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     driver.set_window_size(width=1200, height=720)
#     driver.find_element("id", "checkSizeBtn").click()
#     result = driver.find_element("id", "secret").text
#     print("Result is:", result)