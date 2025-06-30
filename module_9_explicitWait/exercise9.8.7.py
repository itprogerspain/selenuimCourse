from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    wait = WebDriverWait(browser, 50)

    # wait.until(EC.visibility_of_element_located((By.ID, 'closeBtn')))
    wait.until(EC.element_to_be_clickable((By.ID, 'closeBtn'))).click()

    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ad-image')))
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
    print(wait.until(EC.visibility_of_element_located((By.ID, 'message'))).text)


# FS03-R9R3-SVV9-3P05-DSS1-01VI