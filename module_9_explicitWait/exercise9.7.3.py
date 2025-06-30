from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
    wait = WebDriverWait(browser, 10, poll_frequency=0.01)

    browser.find_element(By.ID, 'summonBtn').click()
    wait.until(EC.number_of_windows_to_be(5))
    browser.find_element(By.ID, 'passwordBtn').click()
    alert = wait.until(EC.alert_is_present())
    print(browser.switch_to.alert.text)


# X1Y0-A2B3-Z4XC



# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.7.3/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 60)
#     driver.find_element("id", "summonBtn").click()
#     waiter.until(ec.number_of_windows_to_be(5))
#     driver.find_element("id", "passwordBtn").click()
#     result = waiter.until(ec.alert_is_present()).text
#     print(result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.7.3/index.html")
#     browser.find_element(By.ID, 'summonBtn').click()
#     WebDriverWait(browser, 30).until(EC.number_of_windows_to_be(5))
#     browser.find_element(By.ID, 'passwordBtn').click()
#     print(WebDriverWait(browser, 10).until(EC.alert_is_present()).text)



# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
#
#     driver.find_element(By.ID, 'summonBtn').click()
#
#     WebDriverWait(driver, 20, poll_frequency=0.01).until(EC.number_of_windows_to_be(5))
#     driver.find_element(By.ID, 'passwordBtn').click()
#     print(WebDriverWait(driver, 5).until(EC.alert_is_present()).text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# with webdriver.Chrome() as br:
#     br.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
#     time.sleep(1)  # для загрузки страницы
#
#     summon_button = br.find_element(By.ID, 'summonBtn')  # кнопка призыва страниц
#     password_button = br.find_element(By.ID, 'passwordBtn')  # кнопка для выдачи пароля
#
#     # ожидаем, пока количество страниц не будет равно 5
#     WebDriverWait(br, poll_frequency=0.1, timeout=10).until(EC.number_of_windows_to_be(5))
#
#     # кликаем для получения пароля
#     password_button.click()
#
#     # проверяем наличие alert-окна
#     WebDriverWait(br, 5).until(EC.alert_is_present())
#
#     # извлекаем и выводим пароль
#     password = br.switch_to.alert.text
#     print(password)
