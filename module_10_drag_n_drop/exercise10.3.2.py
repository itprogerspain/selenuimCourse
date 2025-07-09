from selenium import webdriver
import json
import time

options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

with webdriver.Chrome(options=options) as browser:
    browser.get('http://31.130.149.237/json_extraction')
    time.sleep(2)

    logs = browser.get_log("performance")
    total_sum = 0
    for log in logs:
        log_data = json.loads(log["message"])["message"]
        if log_data["method"] == "Network.responseReceived" and "json" in log_data["params"]["response"]["mimeType"].lower():
            response = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": log_data["params"]["requestId"]})
            json_data = json.loads(response["body"])
            for book in json_data.get("data", []):
                total_sum += book.get("id", 0) + book.get("year", 0) + book.get("price", 0)
            print(total_sum)
            break


#   16643




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
#     time.sleep(5)
#     logs_raw = browser.get_log("performance")
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#
#     for log in filter(log_filter, logs):
#         try:
#             request_id = log["params"]["requestId"]
#             resp_url = log["params"]["response"]["url"]
#             body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#             try:
#                 json_data = json.loads(body['body'])
#                 for book in json_data["data"]:
#                     temp = book["id"] + book["year"] + book["price"]
#                     count += temp
#             except Exception as e:
#                 print(f"Ошибка {e}")
#         except WebDriverException:
#             print('Нет Body для данного запроса')
#             continue
# print("Сумма полей: " + str(count))



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
#         count = 0
#         for book in result_json['data']:
#             count += (book['id'] + book['year'] + book['price'])
#         print(count)




# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import WebDriverException
# import json
#
#
# options = Options()
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
#
# # Функция для фильтрации JSON-ответов
# def log_filter(log_):
#     return (log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"])
#
# URL = "http://31.130.149.237/json_extraction"
# with webdriver.Chrome(options=options) as browser:
#     browser.get(url=URL)
#
#     # Получаем "сырые" логи производительности (Performance logs)
#     logs_raw = browser.get_log("performance")
#
#     # Фильтруем и вытаскиваем полезные JSON-сообщения
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#
#     # Перебираем отфильтрованные логи (только JSON-ответы)
#     for log in filter(log_filter, logs):
#         try:
#             request_id = log["params"]["requestId"]
#             resp_url = log["params"]["response"]["url"]
#
#             body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#         except WebDriverException:
#             print('Нет Body для данного запроса')
#             continue
#
#     json_raw = json.loads(body["body"])["data"]
#     result = []
#     for row in json_raw:
#         result.append(row["id"] + row["year"] + row["price"])
#     print("Result is:", sum(result))