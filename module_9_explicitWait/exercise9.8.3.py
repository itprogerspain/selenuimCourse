from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    wait = WebDriverWait(browser, 50)

    wait.until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    print(wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))).text)



# 688596737976