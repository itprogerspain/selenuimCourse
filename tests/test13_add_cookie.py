# Добавление нескольких кукис
import time
from pprint import pprint
from selenium import webdriver

# Список словарей для нескольких cookies
cookies_list = [
    {
        'name': 'cookie1',          # Имя первого cookie
        'value': 'value1',          # Значение первого cookie
        'expiry': 2_000_000_000,    # Время жизни
        'path': '/',                # Путь
        'domain': 'parsinger.ru',   # Домен
        'secure': True,             # Только HTTPS
        'httpOnly': True,           # Ограничение API
        'sameSite': 'Strict'        # Ограничение между сайтами
    },
    {
        'name': 'cookie2',          # Имя второго cookie
        'value': 'value2',          # Значение второго cookie
        'expiry': 2_500_000_000,    # Время жизни (другое значение для примера)
        'path': '/',                # Путь
        'domain': 'parsinger.ru',   # Домен
        'secure': False,            # Не требует HTTPS
        'httpOnly': False,          # Доступ через API
        'sameSite': 'Lax'           # Другое значение sameSite
    },
    {
        'name': 'cookie3',          # Имя третьего cookie
        'value': 'value3',          # Значение третьего cookie
        'expiry': 3_000_000_000,    # Время жизни
        'path': '/',                # Путь
        'domain': 'parsinger.ru',   # Домен
        'secure': True,             # Только HTTPS
        'httpOnly': True,           # Ограничение API
        'sameSite': 'None'          # Без ограничений между сайтами
    }
]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/4/index.html')

    # Добавляем каждый cookie из списка
    for cookie in cookies_list:
        browser.add_cookie(cookie)

    # Выводим все cookies для проверки
    pprint(browser.get_cookies())
    time.sleep(100)

# Добавление одного куки

# import time
# from pprint import pprint
# from selenium import webdriver
#
# cookie_dict = {
#     'name': 'any_name_cookie',    # Любое имя для cookie
#     'value': 'any_value_cookie',  # Любое значение для cookie
#     'expiry': 2_000_000_000,      # Время жизни cookie в секундах
#     'path': '/',                  # Директория на сервере дял которой будут доступны cookie
#     'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
#     'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
#     'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
#     'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
# }
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/4/index.html')
#     browser.add_cookie(cookie_dict)
#     pprint(browser.get_cookies())
#     time.sleep(100)