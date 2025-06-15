import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
    sum = browser.get_window_size()["height"] + browser.get_window_size()["width"]
    browser.find_element(By.ID, 'answer').send_keys(sum)
    browser.find_element(By.ID, 'checkBtn').click()
    print(browser.find_element(By.ID, 'resultMessage').text)
    time.sleep(3)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/8/8.2.2/index.html")
#
#     browser.find_element(By.ID, "answer").send_keys(
#         sum(browser.get_window_size().values())
#     )
#     browser.find_element(By.ID, "checkBtn").click()
#     print(browser.find_element(By.ID, "resultMessage").text.split(": ")[1])




# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/selenium/8/8.2.2/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     size = driver.get_window_size()
#     sum_size = size["width"] + size["height"]
#     driver.find_element("id", "answer").send_keys(sum_size)
#     driver.find_element("id", "checkBtn").click()
#     result = driver.find_element("id", "resultMessage").text
#     print(result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
#     out = sum(browser.get_window_size().values())
#     browser.find_element(By.ID,'answer').send_keys(out)
#     browser.find_element(By.ID, 'checkBtn').click()
#     print(browser.find_element(By.ID,'resultMessage').text)




