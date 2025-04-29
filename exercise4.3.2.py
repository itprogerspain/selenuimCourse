import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    placeholder = browser.find_element(By.ID, "codeInput").send_keys('Дрогон')
    time.sleep(1)
    button = browser.find_element(By.ID, "clickButton").click()
    time.sleep(5)
    answer = browser.find_element(By.ID, 'codeOutput')
    print(answer.text)



# import time
# from selenium import webdriver
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
#     browser.find_element('xpath', '//input').send_keys('Дрогон')
#     browser.find_element('xpath','//button').click()
#     res = browser.find_element('xpath','//pre').text
#     print(res)
#     time.sleep(5)





# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
#
# driver = Chrome()
# driver.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
# field = driver.find_element(By.ID, 'codeInput').send_keys('Дрогон')
# btn = driver.find_element(By.ID, 'clickButton').click()
# answer = driver.find_element(By.ID, 'codeOutput')
# print(answer.text)
# driver.quit()