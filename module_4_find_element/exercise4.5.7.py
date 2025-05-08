import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    all_options = browser.find_elements(By.TAG_NAME, "option")
    count = 0
    for option in all_options:
        count += int(option.text)
    browser.find_element(By.ID, "input_result").send_keys(count)
    browser.find_element(By.ID, "sendbutton").click()
    print(browser.find_element(By.ID, "result").text)
    time.sleep(5)





# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/7/7.html')
#     result = 0
#     for el in browser.find_elements(By.TAG_NAME, 'option'):
#         result += int(el.text)
#     browser.find_element(By.ID, 'input_result').send_keys(result)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(browser.find_element(By.ID, 'result').text)