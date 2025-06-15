from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get("about:blank")
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    time.sleep(1)
    num1 = int(browser.title.translate(str.maketrans('', '', '439')))

    browser.switch_to.new_window('tab')
    browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
    time.sleep(1)
    num2 = int(browser.title.translate(str.maketrans('', '', '780')))
    print(num1 + num2)



# from selenium.webdriver import Chrome
#
#
# URL_1 = "https://parsinger.ru/selenium/8/8.1/site1/"
# URL_2 = "https://parsinger.ru/selenium/8/8.1/site2/"
# with Chrome() as driver:
#     driver.get("about:blank")
#     driver.switch_to.new_window("tab")
#     driver.get(url=URL_1)
#     nums_1 = int(driver.title.replace("4", "").replace("3", "").replace("9", ""))
#     driver.get(url=URL_2)
#     nums_2 = int(driver.title.replace("7", "").replace("8", "").replace("0", ""))
#     print("Result is:", nums_1 + nums_2)




# with webdriver.Chrome() as driver:
#     urls = [
#         'https://parsinger.ru/selenium/8/8.1/site1/',
#         'https://parsinger.ru/selenium/8/8.1/site2/'
#     ]
#
#     titles = []
#     for url in urls:
#         driver.switch_to.new_window('tab')
#         driver.get(url)
#         titles.append(driver.title)
#
#     num1 = ''.join([char for char in titles[0] if char not in '439'])
#     num2 = ''.join([char for char in titles[1] if char not in '780'])
#     total = int(num1) + int(num2)
#
#     print(total)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("about:blank")
#     browser.switch_to.new_window('tab')
#     browser.get('https://parsinger.ru/selenium/8/8.1/site1/')
#     num1 = browser.title
#     for letter in '439':
#         num1 = num1.replace(letter,'')
#     browser.switch_to.new_window('tab')
#     browser.get('https://parsinger.ru/selenium/8/8.1/site2/')
#     num2 = browser.title
#     for letter in '780':
#         num2 = num2.replace(letter,'')
#     print(int(num1) + int(num2))




# import re
#
# from selenium import webdriver
#
# data = [
#     {
#         "url": "https://parsinger.ru/selenium/8/8.1/site1/",
#         "pattern": r'[439]'
#     },
#     {
#         "url": "https://parsinger.ru/selenium/8/8.1/site2/",
#         "pattern": r'[780]'
#     }
# ]
#
# with webdriver.Chrome() as browser:
#     browser.get("about:blank")
#
#     total = 0
#     for properties in data:
#         browser.switch_to.new_window("tab")
#         browser.get(properties["url"])
#         title = browser.title
#         num = re.sub(properties["pattern"], "", title)
#         total += int(num)
#
#     print(total)




# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get("about:blank")
#     time.sleep(1)
#
#     browser.switch_to.new_window('tab')
#     browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
#     num1 = int(''.join(digit for digit in browser.title if digit not in ['4', '3', '9']))
#
#     browser.switch_to.new_window('tab')
#     browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
#     num2 = int(''.join(digit for digit in browser.title if digit not in ['7', '8', '0']))
#
#     print(num1 + num2)





# from selenium_scripts.browser_setup import browser
#
# with browser:
#     nums = []
#     url_nums = (1, 2)
#     chars_to_exclude = (('4', '3', '9'), ('7', '8', '0'))
#
#     for url_num, chars in zip(url_nums, chars_to_exclude):
#         url = f'https://parsinger.ru/selenium/8/8.1/site{url_num}/'
#         browser.get(url)
#         num = int(
#             ''.join([char for char in browser.title if char not in chars])
#         )
#         nums.append(num)
#
#     print(sum(nums))










# title = browser.title
# num1 = title.replace("4","").replace("3", "").replace("9", "")