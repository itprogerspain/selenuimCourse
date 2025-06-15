from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    iframes = browser.find_elements(By.TAG_NAME, 'iframe')
    for i in range(len(iframes)):
        browser.switch_to.frame(iframes[i])
        browser.find_element(By.TAG_NAME, 'button').click()
        code = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        input_ = browser.find_element(By.ID, 'guessInput')
        input_.send_keys(code)
        browser.find_element(By.ID,'checkBtn').click()
        time.sleep(0.3)
        try:
            alert = browser.switch_to.alert.text
            print(alert)
            break
        except NoAlertPresentException:
            input_.clear()



# FD79-32DJ-79XB-124S-P3DX-2456-DFB-DSA9




# from selenium import webdriver
# from selenium.common.exceptions import NoAlertPresentException
#
# URL = "https://parsinger.ru/selenium/5.8/5/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     for i in range(1, 10):
#         iframe = driver.find_element("id", f"iframe{i}")
#         driver.switch_to.frame(iframe)
#         driver.find_element("tag name", "button").click()
#         code = driver.find_element("id", "numberDisplay").text
#         driver.switch_to.default_content()
#         driver.find_element("id", "guessInput").send_keys(code)
#         driver.find_element("id", "checkBtn").click()
#         try:
#             result = driver.switch_to.alert.text
#             print("Result is:", result)
#         except NoAlertPresentException:
#             driver.find_element("id", "guessInput").clear()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/5.8/5/index.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url=url)
#
#     input_field = browser.find_element(By.ID, "guessInput")
#     check_button = browser.find_element(By.ID, "checkBtn")
#     iframes = browser.find_elements(By.TAG_NAME, "iframe")
#
#     for iframe in iframes:
#         input_field.clear()
#         browser.switch_to.frame(iframe)
#         browser.find_element(By.TAG_NAME, "button").click()
#         number = browser.find_element(By.ID, "numberDisplay").text
#         browser.switch_to.default_content()
#         input_field.send_keys(number)
#         check_button.click()
#
#     result = browser.switch_to.alert.text
#     print(result)




# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
#
# with Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
#     inp = browser.find_element(By.ID, 'guessInput')
#     for i in range(9):
#         browser.switch_to.frame(i)
#         browser.find_element(By.TAG_NAME, 'button').click()
#         code = browser.find_element(By.ID, 'numberDisplay').text
#         browser.switch_to.default_content()
#         inp.send_keys(code)
#         browser.find_element(By.ID, 'checkBtn').click()
#         try:
#             print(browser.switch_to.alert.text)
#             break
#         except:
#             pass
#         inp.clear()