from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
    wait = WebDriverWait(browser, 10)
    current_url = browser.current_url
    browser.find_element(By.CLASS_NAME, 'btn').click()
    wait.until(EC.url_changes(current_url))
    print(wait.until(
        EC.visibility_of_element_located((By.ID, 'password'))).text)




# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# URL = "https://parsinger.ru/selenium/9/9.4.4/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("class name", "btn").click()
#     waiter = WebDriverWait(driver, 10, 0.5)
#     waiter.until(EC.url_changes(driver.current_url))
#     result = driver.find_element("id", "password").text
#     print(result)




# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
#
#     driver.find_element(By.XPATH, "//a[text()='Начать']").click()
#     current_url= driver.current_url
#
#     # Вариант №1
#     WebDriverWait(driver, 20).until(EC.url_changes(current_url))
#     print(driver.find_element(By.ID, 'password').text)
#
#     # Вариант №2
#     # print(
#     #     WebDriverWait(driver, 20).until(
#     #         EC.visibility_of_element_located((By.ID, 'password'))
#     #     ).text
#     # )