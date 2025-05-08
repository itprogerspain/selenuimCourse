import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    all_boxes = browser.find_elements(By.CLASS_NAME, "check")
    checked = [box.click() for box in all_boxes]
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)
    time.sleep(5)






# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/4/4.html')
#     all_boxes = browser.find_elements(By.CLASS_NAME, "check")
#     for box in all_boxes:
#         box.click()
#     browser.find_element(By.CLASS_NAME, "btn").click()
#     print(browser.find_element(By.ID, "result").text)
#     time.sleep(5)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/4/4.html')
#     [x.click() for x in browser.find_elements(By.CLASS_NAME, 'check')]
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(browser.find_element(By.ID,'result').text)
#     time.sleep(5)