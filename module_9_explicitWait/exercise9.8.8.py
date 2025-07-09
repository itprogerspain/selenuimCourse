from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    wait = WebDriverWait(browser, 15)

    checkbox = browser.find_element(By.ID, 'myCheckbox')
    if wait.until(EC.element_to_be_selected(checkbox)):
        browser.find_element(By.TAG_NAME, 'button').click()

    print(wait.until(EC.visibility_of(browser.find_element(By.ID, 'result'))).text)


# 34D0-3SCV-SCM0-654R-DVM9-42IU




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# url = "https://parsinger.ru/selenium/5.9/6/index.html"
# with webdriver.Chrome() as browser:
#     try:
#         browser.get(url)
#         wait = WebDriverWait(browser, 30)
#         inp = browser.find_element(By.ID,'myCheckbox')
#
#         WebDriverWait(browser, 10).until(EC.element_to_be_selected(inp))
#         btn = browser.find_element(By.TAG_NAME,'button').click()
#         print(browser.find_element(By.ID,'result').text)
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
