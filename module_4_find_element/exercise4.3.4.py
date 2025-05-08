import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    button = browser.find_element(By.ID, "secret-key-button")
    button.click()
    data_ = button.get_attribute("data")
    print(data_)
    time.sleep(3)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
#     button = browser.find_element(By.ID, "secret-key-button")
#     button.click()
#     print(button.get_attribute("data"))
#
# finally:
#     browser.quit()




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     url = r'https://parsinger.ru/selenium/3/3.2.4/index.html'
#     browser.get(url)
#     time.sleep(1)
#     buttons = browser.find_element(By.CSS_SELECTOR, "div#buttons-container").find_elements(By.CSS_SELECTOR, 'button')
#     for button in buttons:
#         # print(button.text)
#         # print(button.get_attribute('id'))
#         if button.get_attribute('id') == 'secret-key-button':
#             print('секретная кнопка =', button.text)
#             button.click()
#             time.sleep(1)
#             print(button.get_attribute('data'))





# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
#     button = browser.find_element(By.CSS_SELECTOR, '#secret-key-button')
#     button.click()
#     print(button.get_attribute('data'))