from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    wait = WebDriverWait(browser, 10)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    buttons[-1].click()
    wait.until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'))
    print(wait.until(
        EC.visibility_of_element_located((By.ID, 'password'))).text)