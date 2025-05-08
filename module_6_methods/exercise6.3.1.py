from pprint import pprint
from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    print(browser.get_cookie('token_22')['value'])





# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
#     cookies = browser.get_cookies()
#     for cookie in cookies:
#         if cookie['name'] == 'token_22':
#             print(cookie['value'])