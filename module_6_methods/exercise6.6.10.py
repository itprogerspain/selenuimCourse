from selenium import webdriver
from pprint import pprint
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    # pprint(cookies)
    count = 0
    for cookie in cookies:
        try:
            count += int(cookie['value'])
        except ValueError:
            pass
    print(count)




# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#     cookies = browser.get_cookies()
#     res = 0
#     for cookie in cookies:
#         if cookie['name'].startswith('secret_cookie_'):
#             res += int(cookie['value'])
#     print(res)


# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/methods/3/index.html")
#     print(sum(int(cookie["value"]) for cookie in browser.get_cookies() if cookie["name"].startswith("secret_cookie_")))




# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#     cookies = browser.get_cookies()
#     res = 0
#     for cookie in cookies:
#         if cookie['name'].startswith('secret_cookie_'):
#             res += int(cookie['value'])
#     print(res)