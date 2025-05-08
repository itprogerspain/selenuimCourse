import time
from selenium import webdriver
from selenium.webdriver.common.by import By

cookie_dict = {
    'name': 'secretKey',
    'value': 'selenium123',
}

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    browser.add_cookie(cookie_dict)
    browser.refresh()
    print(browser.find_element(By.ID, 'password').text)
    time.sleep(3)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
#     browser.add_cookie({'name': 'secretKey', 'value': 'selenium123'})
#     browser.refresh()
#     print(browser.find_element(By.ID, 'password').text)





# from selenium.webdriver.common.by import By
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
#
#     browser.add_cookie({'name': 'secretKey', 'value': 'selenium123'})
#     browser.refresh()
#
#     password = (
#         browser.find_element(By.CSS_SELECTOR, '#password')
#         .text.split()[1]
#         .strip()
#     )
#     print(password)





# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
#
#     cookie_dict = {
#         'name': 'secretKey',
#         'value': 'selenium123',
#     }
#
#     driver.add_cookie(cookie_dict)
#     driver.refresh()
#
#     print(
#         WebDriverWait(driver, 5).until(
#             EC.visibility_of_element_located((By.ID, 'password'))
#         ).text
#     )




