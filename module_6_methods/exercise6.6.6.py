import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

count = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    elements = browser.find_elements(By.CLASS_NAME, "btn")
    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        count += int(browser.find_element(By.ID, "result").text)
    print(count)







# from selenium import webdriver
# from selenium.webdriver.common.by import By
# url = 'http://parsinger.ru/scroll/4/index.html'
# res = []
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for x in browser.find_elements(By.CLASS_NAME, "btn"):
#         browser.execute_script("return arguments[0].scrollIntoView(true);", x)
#         x.click()
#         res.append(int(browser.find_element(By.ID, 'result').text))
#
# print(sum(res))