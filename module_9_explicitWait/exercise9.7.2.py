from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')

    wait = WebDriverWait(browser, 15)

    browser.find_element(By.CLASS_NAME, 'search-box').send_keys('test')
    browser.find_element(By.ID, 'search-button').click()

    old_result = browser.find_element(By.ID, 'old-result')
    wait.until(EC.staleness_of(old_result))

    wait.until(EC.element_to_be_clickable((By.ID, "secret-button"))).click()

    print(wait.until(EC.visibility_of_element_located((By.ID, 'result'))).text)


# S34RCH-K3Y


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.7.2/index.html")
#     search_box = browser.find_element(By.CLASS_NAME, "search-box")
#     search_box.send_keys("test")
#     search_button = browser.find_element(By.ID, "search-button")
#     search_button.click()
#
#     # Находим старый результат
#     old_result = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "old-result"))
#     )
#     print("Найден старый результат. Ждем, пока он исчезнет...")
#
#     # КЛЮЧЕВОЙ МОМЕНТ: ждем, пока старый результат не исчезнет из DOM
#     WebDriverWait(browser, 10).until(
#         EC.staleness_of(old_result)
#     )
#     print("Старый результат исчез! Ищем кнопку секрета в новом результате...")
#
#     # Находим и нажимаем кнопку секрета в новом результате
#     secret_button = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.ID, "secret-button"))
#     )
#
#     secret_button.click()
#
#     # Получаем пароль
#     result = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.ID, "result"))
#     )
#
#     password = result.text
#     print(f"Получен пароль: {password}")
#
#     # Небольшая пауза, чтобы увидеть результат
#     time.sleep(3)
#
# print("Готово!")





# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.7.2/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("class name", "search-box").send_keys("Лысый еж")
#     driver.find_element("id", "search-button").click()
#     WebDriverWait(driver, 30).until(ec.element_to_be_clickable(("id", "secret-button"))).click()
#     result = driver.find_element("id", "result").text
#     print("Result is:", result)





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
#     browser.get("https://parsinger.ru/selenium/9/9.7.2/index.html")
#     browser.find_element(By.CLASS_NAME, 'search-box').send_keys('test')
#
#     browser.find_element(By.ID, 'search-button').click()
#     WebDriverWait(browser, 10).until(EC.staleness_of(browser.find_element(By.ID, 'old-result')))
#     browser.find_element(By.ID, 'secret-button').click()
#
#     print(browser.find_element(By.ID, 'result').text)




