from selenium import webdriver
import json
import time

options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

with webdriver.Chrome(options=options) as browser:
    browser.get('http://31.130.149.237/json_extraction')
    time.sleep(2)

    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    logs = browser.get_log("performance")
    passwords = []
    for log in logs:
        log_data = json.loads(log["message"])["message"]
        if log_data["method"] == "Network.responseReceived" and "json" in log_data["params"]["response"][
            "mimeType"].lower():
            response = browser.execute_cdp_cmd("Network.getResponseBody",
                                               {"requestId": log_data["params"]["requestId"]})
            json_data = json.loads(response["body"])
            for book in json_data.get("data", []):
                if "password" in book:
                    passwords.append(book["password"])

    print("-".join(passwords))



# JSON-EXTRACTION-POWER-SUM-BOOKS-PASS


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import json
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
# URL = "http://31.130.149.237/json_extraction"
# with webdriver.Chrome(options=options) as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     end_of_page = driver.find_element("id", "endMessage")
#     books_container = driver.find_element("class name", "books-container")
#     count = 0
#     while count < 10:
#         action.move_to_element(books_container).scroll_by_amount(0, 1000).perform()
#         count += 1
#
#     # Получаем "сырые" логи производительности (Performance logs)
#     logs_raw = driver.get_log("performance")
#
#     # Фильтруем и вытаскиваем полезные JSON-сообщения
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#
#     result = []
#
#     # Перебираем отфильтрованные логи (только JSON-ответы)
#     for log in filter(log_filter, logs):
#         try:
#             request_id = log["params"]["requestId"]
#             body = driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#             result_json = json.loads(body["body"])
#             for row in result_json["data"]:
#                 if "password" in row:
#                     result.append(row["password"])
#         except WebDriverException:
#             print('Нет Body для данного запроса')
#             continue
#     print("Result is:", "-".join(result))





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
#     for _ in range(18):
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(1)
#     # Получаем "сырые" логи производительности (Performance logs)
#     logs_raw = browser.get_log("performance")
#     # Фильтруем и вытаскиваем полезные JSON-сообщения
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#     # Перебираем отфильтрованные логи (только JSON-ответы)
#     password = []
#     for log in filter(log_filter, logs):
#         request_id = log["params"]["requestId"]
#         resp_url = log["params"]["response"]["url"]
#
#         body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#         result_json = json.loads(body["body"])
#         for book in result_json['data']:
#             if 'password' in book.keys():
#                 password.append(book['password'])
#     print('-'.join(password))





# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import WebDriverException
# import json
# import time
#
# URL = "http://31.130.149.237/json_extraction"
# options = Options()
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
# password_parts = []
#
# def log_filter(log_):
#     return (log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"])
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get(URL)
#     time.sleep(1)
#     last_height = browser.execute_script("return document.body.scrollHeight")
#     while True:
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         new_height = browser.execute_script("return document.body.scrollHeight")
#         time.sleep(.5)
#         if new_height == last_height:
#             break
#         last_height = new_height
#     logs_raw = browser.get_log("performance")
#     logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
#     for log in filter(log_filter, logs):
#         try:
#             request_id = log["params"]["requestId"]
#             resp_url = log["params"]["response"]["url"]
#             body = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
#             try:
#                 json_data = json.loads(body['body'])
#                 for book in json_data["data"]:
#                     temp = book.get("password", "")
#                     if temp:
#                         password_parts.append(temp)
#             except Exception as e:
#                 print(f"Ошибка {e}")
#         except WebDriverException:
#             print('Нет Body для данного запроса')
#             continue
# final_password = "-".join(password_parts)
# print("Сумма полей: " + final_password)



