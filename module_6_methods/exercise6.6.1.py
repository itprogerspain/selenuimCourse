import time
from selenium import webdriver
from selenium.webdriver.common.by import By


count = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    result = browser.find_element(By.ID, "result").text.lower()
    if result.isdigit():
        print(result, count)
    else:
        while True:
            browser.refresh()
            count += 1
            time.sleep(3)
            result = browser.find_element(By.ID, "result").text.lower()
            if result.isdigit():
                print(result, count)
                break




# from selenium import webdriver
#
# URL = "https://parsinger.ru/methods/1/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     while True:
#         result = driver.find_element("id", "result").text
#         if result.isdigit():
#             print("Result is:", result)
#             break
#         else:
#             driver.refresh()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/1/index.html')
#
#     while True:
#         text = browser.find_element(By.ID, 'result').text.lower()
#         if text != 'refresh page':
#             print(text)
#             break
#         else:
#             browser.refresh()





from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/1/index.html")
    while not (digit := browser.find_element('id', 'result').text).isdigit():
        browser.refresh()
        continue
    print(f'Наше число -> {digit}')