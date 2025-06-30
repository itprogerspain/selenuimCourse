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




# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/5.9/4/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 20)
#     waiter.until(ec.element_to_be_clickable(("id", "closeBtn"))).click()
#     if waiter.until(ec.invisibility_of_element_located(("id", "ad"))):
#         driver.find_element("css selector", ".box>button").click()
#         result = driver.find_element("id", "message").text
#         print("Result is:", result)
#     else:
#         print("Try again!")




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Инициализация и запуск браузера в конструкции with
# with webdriver.Chrome() as browser:
#     # Открываем страницу
#     browser.get("https://parsinger.ru/selenium/5.9/4/index.html")
#     wait = WebDriverWait(browser, 15)
#
#     # Ждем, пока таймер исчезнет и появится крестик
#     close_button = wait.until(EC.visibility_of_element_located((By.ID, "closeBtn")))
#     wait.until(EC.element_to_be_clickable((By.ID, "closeBtn")))
#     close_button.click()
#
#     # Ждем, пока реклама полностью исчезнет (будет удалена из DOM)
#     wait.until(EC.invisibility_of_element_located((By.ID, "ad")))
#
#     # Нажимаем на кнопку "Нажми на меня"
#     button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
#     button.click()
#     # Получаем секретное значение
#     message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
#     secret_value = message.text
#     # Выводим результат
#     print(f"Секретное значение: {secret_value}")
#     time.sleep(3)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
#     ads_locator = (By.ID, 'ad')
#     ads_button_locator = (By.ID, 'closeBtn')
#     ads_button = WebDriverWait(browser, 60).until(EC.element_to_be_clickable(ads_button_locator))
#     ads_button.click()
#     WebDriverWait(browser, 60).until(EC.invisibility_of_element_located(ads_locator))
#     browser.find_element(By.TAG_NAME, 'button').click()
#     print(browser.find_element(By.ID, 'message').text)




# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/4/index.html')
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "closeBtn"))).click()
#     time.sleep(5)
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Нажми на меня"]'))).click()
#     print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'message'))).text)




# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# url = 'https://parsinger.ru/selenium/5.9/4/index.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.execute_script(f"document.body.style.zoom = '50%'")
#     browser.find_element(By.CLASS_NAME, 'close').click()
#     WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'ad')))
#     browser.find_element(By.TAG_NAME, 'button').click()
#     print(browser.find_element(By.ID, 'message').text)+




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
#     wait = WebDriverWait(browser, 10)
#
#     close_btn = browser.find_element(By.CLASS_NAME, 'close')
#     browser.execute_script("arguments[0].click();", close_btn)
#
#     wait.until(EC.invisibility_of_element_located((By.ID, 'ad')))
#
#     browser.find_element(By.CSS_SELECTOR, '.box button').click()
#     print(browser.find_element(By.ID, 'message').text)