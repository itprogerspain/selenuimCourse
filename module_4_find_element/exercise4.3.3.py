import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    showTextButton = browser.find_element(By.ID, "showTextBtn").click()
    text1 = browser.find_element(By.ID, "text1").text
    input_ = browser.find_element(By.ID, "userInput").send_keys(text1)
    checkButton = browser.find_element(By.ID, "checkBtn").click()
    time.sleep(5)
    answer = browser.find_element(By.ID, 'text2')
    print(answer.text)



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     url = r'https://parsinger.ru/selenium/3/3.2.3/index.html'
#     browser.get(url)
#     time.sleep(1)
#     button_id = browser.find_element(By.CSS_SELECTOR, "button#showTextBtn").click()
#     button_code = browser.find_element(By.CSS_SELECTOR, "div#text1").text
#     button_input = browser.find_element(By.CSS_SELECTOR, "input#userInput").send_keys(button_code)
#     button_check = browser.find_element(By.CSS_SELECTOR, "button#checkBtn").click()
#     time.sleep(1)
#     button_pw = browser.find_element(By.CSS_SELECTOR, "div#text2").text
#     print(button_pw)




# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
#     browser.find_element(By.CSS_SELECTOR, '#showTextBtn').click()
#     password = browser.find_element(By.CSS_SELECTOR, '#text1').text
#     browser.find_element(By.CSS_SELECTOR, '#userInput').send_keys(password)
#     browser.find_element(By.CSS_SELECTOR, '#checkBtn').click()
#     code = browser.find_element(By.CSS_SELECTOR, '#text2').text
#     print(code)




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
#
#     button = browser.find_element(By.ID, 'showTextBtn')
#     button.click()
#
#     text = browser.find_element(By.ID, 'text1').text
#
#     input = browser.find_element(By.ID, "userInput")
#     input.send_keys(text)
#
#     button_check = browser.find_element(By.ID, 'checkBtn')
#     button_check.click()
#
#     text = browser.find_element(By.ID, 'text2').text
#     print(text)
#
#     time.sleep(4)






# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
# browser.find_element(By.ID, 'showTextBtn').click()
# browser.find_element(By.ID, 'userInput').send_keys(
#     browser.find_element(By.ID, 'text1').text)
# browser.find_element(By.ID, 'checkBtn').click()
# print(browser.find_element(By.ID, 'text2').text)
# time.sleep(3)
# browser.quit()

