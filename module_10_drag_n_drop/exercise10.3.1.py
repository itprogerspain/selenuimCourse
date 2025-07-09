from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

with webdriver.Chrome(options=options) as browser:
    browser.get('http://31.130.149.237/json_extraction')
    wait = WebDriverWait(browser, 15)
    contacts_button = wait.until(EC.element_to_be_clickable((By.ID, "contactsButton")))
    browser.execute_script("arguments[0].click();", contacts_button)
    time.sleep(5)

    logs = browser.get_log("performance")
    for log in logs:
        log_data = json.loads(log["message"])["message"]
        if log_data["method"] == "Network.responseReceived" and "json" in log_data["params"]["response"]["mimeType"].lower():
            response = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": log_data["params"]["requestId"]})
            json_data = json.loads(response["body"])
            for item in json_data.get('stores', []):
                if item.get("id") == 2:
                    print(item.get("coordinates", {}).get("lng"))
                    break



#   30.332



# # Selenium-Wire
#
# from seleniumwire import webdriver
# import time
# import json
# import gzip
#
# URL = 'http://31.130.149.237/json_extraction'
# options = webdriver.ChromeOptions()
# # Отключаем автоматическое обновление HTTP до HTTPS т.к. тренажер работает на 80 порту HTTP
# options.add_argument('--disable-features=HttpsUpgrades')
# count = 0
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get(URL)
#     contact_button = browser.find_element("id", "contactsButton")
#     contact_button.click()
#     time.sleep(1)
#     json_count = 0
#     for request in browser.requests:
#         if (request.response and
#             'application/json' in request.response.headers.get('Content-Type', '') and
#             len(request.response.body) > 150):
#             json_count += 1
#             try:
#                 body = request.response.body
#                 if request.response.headers.get('Content-Encoding') == 'gzip':
#                     body = gzip.decompress(body)
#                 decoded_body = body.decode('utf-8', errors='replace')
#                 json_data = json.loads(decoded_body)
#                 filename = f"json_{json_count}.json"
#                 with open(filename, 'w', encoding='utf-8') as f:
#                     json.dump(json_data, f, indent=4, ensure_ascii=False)
#                 print(f"Сохранено в файл: {filename}")
#             except Exception as e:
#                 print(f"Ошибка при обработке ответа #{json_count}: {str(e)}")
#                 # Сохраняем проблемное тело ответа для анализа
#                 with open(f"error_response_{json_count}.txt", 'w', encoding='utf-8') as f:
#                     f.write(decoded_body if 'decoded_body' in locals() else "Ошибка декодирования")




# # CDP
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import WebDriverException
# import json
# import time
#
# URL = "http://31.130.149.237/json_extraction"
# options = Options()
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
# count = 0
#
# def log_filter(log_):
#     return (log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"])
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get(URL)
#     contact_button = browser.find_element("id", "contactsButton")
#     contact_button.click()
#     time.sleep(1)
#     logs_raw = browser.get_log("performance")
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#     json_count = 0
#     for log in filter(log_filter, logs):
#         try:
#             request_id = log["params"]["requestId"]
#             resp_url = log["params"]["response"]["url"]
#             json_count += 1
#             body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#             try:
#                 json_data = json.loads(body['body'])
#                 filename = f"json_{json_count}.json"
#                 with open(filename, 'w', encoding='utf-8') as f:
#                     json.dump(json_data, f, indent=4, ensure_ascii=False)
#                 print(f"Сохранено в файл: {filename}")
#             except Exception as e:
#                 print(f"Ошибка {e}")
#         except WebDriverException:
#             print('Нет Body для данного запроса')
#             continue





# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import json
# import time
#
# options = Options()
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
#
#
# # Функция для фильтрации JSON-ответов
# def log_filter(log_):
#     return (log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"])
#
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("http://31.130.149.237/json_extraction")
#     time.sleep(2)
#     # Если нужно — можно инициировать события тут, например клик или ввод
#     browser.find_element("id", "contactsButton").click()
#     time.sleep(2)
#     # Получаем "сырые" логи производительности (Performance logs)
#     logs_raw = browser.get_log("performance")
#     # Фильтруем и вытаскиваем полезные JSON-сообщения
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#     # Перебираем отфильтрованные логи (только JSON-ответы)
#     for log in filter(log_filter, logs):
#         request_id = log["params"]["requestId"]
#         resp_url = log["params"]["response"]["url"]
#
#         body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#         result_json = json.loads(body["body"])
#         try:
#             print(result_json["stores"][1]["coordinates"]["lng"])
#         except:
#             pass





from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import json
import time

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})


# Функция для фильтрации JSON-ответов
def log_filter(log_):
    return (log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"])

URL = "http://31.130.149.237/json_extraction"
with webdriver.Chrome(options=options) as browser:
    browser.get(url=URL)
    time.sleep(2)

    # Если нужно — можно инициировать события тут, например клик или ввод
    browser.find_element("id", "contactsButton").click()

    time.sleep(2)

    # Получаем "сырые" логи производительности (Performance logs)
    logs_raw = browser.get_log("performance")

    # Фильтруем и вытаскиваем полезные JSON-сообщения
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

    # Перебираем отфильтрованные логи (только JSON-ответы)
    for log in filter(log_filter, logs):
        try:
            request_id = log["params"]["requestId"]
            resp_url = log["params"]["response"]["url"]

            body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
        except WebDriverException:
            print('Нет Body для данного запроса')
            continue
    result_json = json.loads(body["body"])
    print("Result is:", result_json["stores"][1]["coordinates"]["lng"])