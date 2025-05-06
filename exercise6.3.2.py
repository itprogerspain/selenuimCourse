from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    cookies = browser.get_cookies()
    for cookie in cookies:
        song = cookie['name']
    browser.find_element(By.ID, 'phraseInput').send_keys(song)
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'result').text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
#     browser.find_element(By.ID, 'phraseInput').send_keys(
#         browser.get_cookies()[0]['name'])
#     browser.find_element(By.ID, 'checkButton').click()
#     print(browser.find_element(By.ID, 'result').text)