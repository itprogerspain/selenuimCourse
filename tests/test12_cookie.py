from pprint import pprint
from selenium import webdriver
import time

# test 1 - .get_cookies()
with webdriver.Chrome() as browser:
    browser.get('https://ya.ru/')
    cookies = browser.get_cookies()
    pprint(cookies)

# test 2 - .get_cookie(name_cookie) - 2.1
with webdriver.Chrome() as browser:
    browser.get('https://ya.ru/')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение


# test 3 (лучше использовать этот способ) - .get_cookie(name_cookie) - 2.2
with webdriver.Chrome() as browser:
    browser.get('https://ya.ru/')
    print(browser.get_cookie('_ym_uid')['expiry'])


# test 4 - .delete_cookie(name_cookie)
with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/methods/3/index.html"
    browser.get(url)
# Итерируемся по всем именам куков, в которых последнее число — чётное, и удаляем их.
    for i in range(0,17,2):
        browser.delete_cookie(f"secret_cookie_{i}")
    time.sleep(30)


# test 5 - .delete_all_cookies()
with webdriver.Chrome() as browser:
    url = "https://parsinger.ru/methods/3/index.html"
    browser.get(url)

    # Получаем список существующих кук до удаления
    print("Cookies before deletion:")
    pprint(browser.get_cookies())

    # Удаляем все куки
    browser.delete_all_cookies()

    # Проверяем, что куки удалены
    print("\nCookies after deletion:")
    pprint(browser.get_cookies())
