from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.3.2/index.html")
    browser.delete_all_cookies()
    print(browser.find_element(By.ID, 'password').text)




# driver.get("https://parsinger.ru/selenium/6/6.3.2/index.html")
# driver.delete_all_cookies()
# res = driver.find_element('xpath', '//p[@id="password"]').text
# res = res.split()
# pprint(res[1])



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
# browser.delete_all_cookies()
# while True:
#     pass