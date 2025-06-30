from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')
    wait = WebDriverWait(browser, 50)

    wait.until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    if wait.until(EC.title_contains('JK8HQ')): # можно обойтись и без if
        print(browser.title)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# url = 'http://parsinger.ru/expectations/4/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
#     if WebDriverWait(browser, 30).until(EC.title_contains('JK8HQ')):
#         print(browser.execute_script("return document.title;"))




# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "http://parsinger.ru/expectations/4/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     WebDriverWait(driver, 30).until(ec.element_to_be_clickable(("id", "btn"))).click()
#     WebDriverWait(driver, 30).until(ec.title_contains("JK8HQ"))
#     result = driver.title
#     print("Result is:", result)