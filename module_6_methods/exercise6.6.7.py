import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

count = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    elements = browser.find_elements(By.CLASS_NAME, "parent")
    for element in elements:
        box = element.find_element(By.CLASS_NAME, "checkbox")
        if box.is_selected():
            count += int(element.find_element(By.TAG_NAME, "textarea").text)
    print(count)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# count = 0
# url = 'https://parsinger.ru/selenium/5.5/3/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     parents = browser.find_elements(By.CLASS_NAME,'parent')
#     for elem in parents:
#         if elem.find_element(By.CLASS_NAME,'checkbox').is_selected() == True:
#             count += int(elem.text)
#     time.sleep(5)
# print(count)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.5/3/1.html")
#     res = sum(
#         int(i.find_element(By.TAG_NAME, "textarea").text)
#         for i in browser.find_elements(By.CLASS_NAME, "parent")
#         if i.find_element(By.CLASS_NAME, "checkbox").is_selected()
#     )
#     print(res)




# result = 0
# for element in browser.find_elements(By.CSS_SELECTOR, 'div.parent'):
#     num = element.find_element(By.TAG_NAME, "textarea").text
#     check = element.find_element(By.TAG_NAME, "input").is_selected()
#     if check:
#         result += int(num)
# print(result)