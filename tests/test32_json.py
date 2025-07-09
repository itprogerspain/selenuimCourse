from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json
import time


# Настраиваем Chrome с включением логов производительности
options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})  # Включаем логи сетевых запросов

with webdriver.Chrome(options=options) as browser:
    # Открываем страницу
    browser.get('http://31.130.149.237/json_extraction')  # Замените на ваш URL
    wait = WebDriverWait(browser, 15)

    # Ждем 2 секунды, чтобы страница сделала запросы


    time.sleep(2)

    # Получаем все логи производительности
    logs = browser.get_log("performance")

    # Фильтруем логи, чтобы найти JSON-ответы
    for log in logs:
        log_data = json.loads(log["message"])["message"]
        if log_data["method"] == "Network.responseReceived" and "json" in log_data["params"]["response"]["mimeType"]:
            request_id = log_data["params"]["requestId"]
            try:
                # Получаем тело ответа (JSON)
                response = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                json_data = json.loads(response["body"])  # Преобразуем строку JSON в Python-объект
                print("Найден JSON:", json_data)
            except Exception as e:
                print(f"Ошибка при получении JSON: {e}")



# # Версия с Selenium Wire
#
# # pip install selenium-wire
#
# from seleniumwire import webdriver
# import time
# import json
#
# # Настраиваем браузер
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# with webdriver.Chrome(options=options) as browser:
#     # Открываем страницу
#     browser.get('https://parsinger.ru/json_extraction/1/index.html')  # Замените на ваш URL
#     time.sleep(2)  # Ждем, пока страница сделает запросы
#
#     # Перебираем все запросы
#     for request in browser.requests:
#         if request.response and 'application/json' in request.response.headers.get('Content-Type', ''):
#             try:
#                 json_data = json.loads(request.response.body.decode('utf-8'))
#                 print("Найден JSON:", json_data)
#             except Exception as e:
#                 print(f"Ошибка при обработке JSON: {e}")
