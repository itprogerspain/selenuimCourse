from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    wait = WebDriverWait(browser, 10)
    while True:
        browser.find_element(By.LINK_TEXT, 'Искать бананы').click()
        try:
            wait.until(EC.url_contains("qLChv49"))
            browser.find_element(By.ID, 'checkButton').click()
            print(wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, 'p'))).text)
            break
        except TimeoutException:
            continue


# N0-M0R3-HUNGRY-M0NK3Y




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
#
# URL = "http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html"
# url_template = "qLChv49"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     try:
#         while not WebDriverWait(driver, 0.5).until_not(ec.url_contains(url_template)):
#             driver.find_element("id", "searchLink").click()
#     except TimeoutException:
#         driver.find_element("id", "checkButton").click()
#         result = driver.find_element("id", "result").text
#         print(result)






# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# print("Запускаем поиск банана для Абу...")
# with webdriver.Chrome() as browser:
#     browser.get("http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html")
#     print("Начинаем поиск. Абу готов к приключению!")
#     attempt = 1
#     while True:
#         print(f"\nПопытка #{attempt}: Абу ищет бананы...")
#         link = browser.find_element(By.ID, "searchLink")
#         link.click()
#
#         try:
#             WebDriverWait(browser, 0.6).until(EC.url_contains("qLChv49"))
#             print("Ура! Абу нашёл нужную страницу!")
#             check_btn = browser.find_element(By.ID, "checkButton")
#             check_btn.click()
#             result = browser.find_element(By.CSS_SELECTOR, "p")
#             print(f"Победа! Абу получил пароль: {result.text}")
#             break
#         except:
#             print("Здесь банана нет, продолжаем поиск...")
#             attempt += 1
#             continue
#
# print("Поиск завершён. Абу доволен!")


