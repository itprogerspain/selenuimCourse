from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    count = 0
    for cookie in cookies:
        if int(cookie["name"].split('_')[-1]) % 2 == 0:
               count += int(cookie["value"])
    print(count)




# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/3/index.html')
#     print(sum(int(c['value']) for c in browser.get_cookies() if int(c['name'].split('_')[-1]) % 2 == 0))


