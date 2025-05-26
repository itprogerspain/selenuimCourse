import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

links = []
cookies = []
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    elements = browser.find_elements(By.TAG_NAME, "a")
    for element in elements:
        link = element.get_attribute('href')
        links.append(link)
    # time.sleep(3)
    # pprint(links)
    for link in links:
        browser.get(link)
        cookie = browser.get_cookies()
        cookies.append(cookie[0]['expiry'])
    # pprint(cookies)
    item, value = max(zip(cookies, links), key=lambda x: x[0])
    browser.get(value)
    print(browser.find_element(By.ID, "result").text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     links = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
#     res = []
#     for link in links:
#         browser.get(link)
#         res.append((link, browser.get_cookies()[0]['expiry']))
#     res_link = max(res, key=lambda x: x[1])[0]
#     browser.get(res_link)
#     print(browser.find_element(By.ID, 'result').text)







# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     link = [x.find_element(By.TAG_NAME, 'a') for x in browser.find_elements(By.CLASS_NAME, 'urls')]
#     res = []
#     while True:
#         for x, br in zip(link, range(1, len(link) + 1)):
#             browser.get(x.get_attribute('href'))
#             code = browser.find_element(By.ID, 'result').text
#             browser.back()
#             res.append({
#                 'expiry': [x['expiry'] for x in browser.get_cookies()],
#                 'code': code,
#             })
#         if br == len(link):
#             break
#     print(int(sorted(res, key=lambda x: x['expiry'], reverse=True)[0]['code']))
#
#





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/5/index.html')
#     data = webdriver.find_elements(By.XPATH, "//div[@class='urls']/a")
#     links = [elem.get_attribute('href') for elem in data]
#     expiry_dates = {}
#     for link in links:
#         webdriver.get(link)
#         num = int(webdriver.find_element(By.ID, 'result').text)
#         cookies = webdriver.get_cookies()
#         for cookie in cookies:
#             expiry_dates[num] = int(cookie['expiry'])
#     print(max(expiry_dates, key=expiry_dates.get))



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     elements = browser.find_elements(By.TAG_NAME, 'a')
#     links=[]
#     all_cookie = []
#     for element in elements:
#         links.append(element.get_attribute('href'))
#     for link in links:
#         browser.get(link)
#         cookie = browser.get_cookie('foo2')
#         all_cookie.append((cookie['expiry'], browser.find_element(By.ID, 'result').text))
#     all_cookie.sort()
#     print(all_cookie[-1][1])


