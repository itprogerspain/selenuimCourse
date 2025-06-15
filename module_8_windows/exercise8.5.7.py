from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')
    count = 0
    for i in range(10):
        buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
        buttons[i].click()
        browser.switch_to.window(browser.window_handles[-1])
        number = int(browser.title)
        count += number
        browser.find_element(By.TAG_NAME, 'a').click()  # можно заменить на следующий вариант:

        # альтернатива

        # browser.close()
        # browser.switch_to.window(browser.window_handles[0])

    print(count)




# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/blank/3/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     buttons = driver.find_elements("class name", "buttons")
#     result = []
#     for button in buttons:
#         button.click()
#     for handle in driver.window_handles[1:]:
#         driver.switch_to.window(handle)
#         result.append(int(driver.title))
# print("Result is:", sum(result))



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     count = 0
#     browser.get('http://parsinger.ru/blank/3/index.html')
#     [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
#     tabs = browser.window_handles
#     for tab in range(len(tabs)):
#         browser.switch_to.window(browser.window_handles[tab])
#         title = browser.execute_script("return document.title;")
#         if title.isdigit():
#             count += (int(browser.execute_script("return document.title;")))
#     print(count)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import re
# total = 0
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/blank/3/index.html')
#     btns = browser.find_elements(By.CLASS_NAME, 'buttons')
#     for btn in btns:
#         btn.click()
#         time.sleep(.3)
#     for i in browser.window_handles:
#         browser.switch_to.window(i)
#         title = browser.title
#         if title.isdigit():
#             total += int(title)
#     print(total)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pprint import pprint
#
# browser= webdriver.Chrome()
# browser.get("http://parsinger.ru/blank/3/index.html")
# print("start=", browser.current_window_handle)
# list_input = browser.find_elements(By.CSS_SELECTOR, 'input[type="button"]')
#
# for el in list_input:
#     el.click()
#
# summa = 0
# descriptors = browser.window_handles
# print("descriptors:")
# pprint(descriptors)
# for deskr in descriptors[1:]:
#     browser.switch_to.window(deskr)
#     summa += int(browser.title)
#
# print("summa=", summa)




# from selenium.webdriver.common.by import By
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/blank/3/index.html')
#
#     buttons = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
#     for button in buttons:
#         button.click()
#
#     titles = []
#     tabs = browser.window_handles
#     for tab in tabs:
#         browser.switch_to.window(tab)
#         title = browser.title
#         if title.isdigit():
#             titles.append(int(title))
#
#     print(sum(titles))




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://parsinger.ru/blank/3/index.html'
# result = []
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     main_window = browser.current_window_handle
#     buttons = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
#     for button in buttons:
#         button.click()
#     browser.switch_to.window(main_window)
#     browser.close()
#     windows = browser.window_handles
#     for window in windows:
#         if window is not main_window:
#             browser.switch_to.window(window)
#             result.append(int(browser.title))
#     print(sum(result))