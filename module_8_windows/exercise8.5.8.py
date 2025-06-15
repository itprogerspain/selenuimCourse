from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

count = 0
with webdriver.Chrome() as browser:
    for url in sites:
        browser.get(url)

        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        result = browser.find_element(By.ID, 'result').text
        count += int(result) ** 0.5
print(round(count, 9))



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# total = 0
#
# sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
#          'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
# with webdriver.Chrome() as browser:
#     for i in range(len(sites)):
#         time.sleep(1)
#         browser.execute_script(f'window.open("{sites[i]}", "_blank")')
#         browser.switch_to.window(browser.window_handles[-1])
#         check = browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         time.sleep(.1)
#         result = math.sqrt(int(browser.find_element(By.ID, 'result').text))
#         total += result
#
# print(round(total,9))



# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
#          'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
#
# with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
#     for site in sites:
#         driver.execute_script(f"window.open('{site}');")
#         time.sleep(1)
#     total = 0
#     for el in driver.window_handles[1:]:
#         driver.switch_to.window(el)
#         check = driver.find_element("xpath","//input[@type='checkbox']").click()
#         res = driver.find_element("xpath","//span[@id='result']").text
#         total += int(res)**0.5
#         time.sleep(1)
#
#     print(round(total,9))



# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# result = []
# with webdriver.Chrome() as browser:
#     for x in range(1, 7):
#         blank = browser.execute_script(f'window.open("http://parsinger.ru/blank/1/{x}.html", "_blank{x}");')
#     tabs = browser.window_handles
#     for z in range(len(tabs) - 1):
#         if not browser.execute_script("return document.title;"):
#             browser.close()
#         browser.switch_to.window(browser.window_handles[z])
#         browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         result.append(math.sqrt(int(browser.find_element(By.ID, 'result').text)))


