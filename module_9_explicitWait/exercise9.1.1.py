import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    wait = WebDriverWait(browser, 15)
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
    for i in range(1, 5):
        wait.until(EC.element_to_be_clickable((By.ID, f"button{i}"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "finalButton"))).click()
    print(browser.find_element(By.ID, 'message').text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# url = "https://parsinger.ru/selenium/9/9.1.1/index.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     buttons = browser.find_elements(By.XPATH, "//button")
#
#     for button in buttons:
#         WebDriverWait(browser, 50).until(EC.element_to_be_clickable(button)).click()
#
#     print(browser.find_element(By.ID,'message').text)



# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.1.1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     buttons = driver.find_elements("css selector", ".button-container button")
#     waiter = WebDriverWait(driver, timeout=15, poll_frequency=0.5)
#     for button in buttons:
#         waiter.until(EC.element_to_be_clickable(button)).click()
#     result = driver.find_element("id", "message").text
#     print(result)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
#
#     # Ожидание и нажатие на Кнопку 1
#     button1 = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.ID, 'button1')))
#     button1.click()
#
#     # Ожидание и нажатие на Кнопку 2
#     button2 = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.ID, 'button2')))
#     button2.click()
#
#     # Ожидание и нажатие на Кнопку 3
#     button3 = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.ID, 'button3'))
#     )
#     button3.click()
#
#     # Ожидание и нажатие на Кнопку 4
#     button4 = WebDriverWait(browser, 15).until(
#         EC.element_to_be_clickable((By.ID, 'button4')))
#     button4.click()
#
#     final_btn = browser.find_element(By.ID, 'finalButton')
#     final_btn.click()
#     password = browser.find_element(By.ID, 'message')
#     print(f"Пароль = {password.text.split(": ")[1]}")
#     time.sleep(5)
