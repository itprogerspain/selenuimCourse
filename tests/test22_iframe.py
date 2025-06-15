from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/4/index.html')

    # Переключаемся на iframe
    iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe_element)

    # Извлекаем HTML содержимое из iframe
    iframe_content = browser.page_source

    print(iframe_content)
    time.sleep(30)