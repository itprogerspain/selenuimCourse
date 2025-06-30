from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    wait = WebDriverWait(browser, 50)

    wait.until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
    alert = wait.until(EC.alert_is_present())
    print(browser.switch_to.alert.text)


# tlprcp6S-kDbhujKo-uh7Rv9f9-irv26iU9-Zt2XZcIm




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/5.9/2/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 60)
#     waiter.until(ec.visibility_of_element_located(("id", "qQm9y1rk"))).click()
#     result = waiter.until(ec.alert_is_present()).text
#     print("Result is:", result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# url = "https://parsinger.ru/selenium/5.9/2/index.html"
#
# with webdriver.Chrome() as browser:
#     try:
#         print("Открываем страницу тренажера...")
#         browser.get(url)
#         print('Настраиваемся на работу...')
#         wait = WebDriverWait(browser, 30)
#         print('Поехали...')
#
#
#         class_btn = wait.until(EC.presence_of_element_located((By.ID, 'qQm9y1rk')))
#         class_btn.click()
#
#         alert = wait.until(EC.alert_is_present())
#         text = alert.text
#         alert.accept()
#         print(text)
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")