import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    elements = browser.find_elements(By.CSS_SELECTOR, ".block")
    for element in elements:
        btn = element.find_element(By.CSS_SELECTOR, ".button").click()
    password = browser.find_element(By.TAG_NAME, "password")
    print(password.text)
    time.sleep(5)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/3/3.3.2/index.html")
#     block = browser.find_elements(By.CLASS_NAME, 'block')
#     for element in block:
#         element.find_element(By.CLASS_NAME, 'button').click()
#
#     password = browser.find_element(By.TAG_NAME, 'password').text
#     print(password)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
#     for block in browser.find_elements(By.CLASS_NAME, "block"):
#         block.find_element(By.TAG_NAME, "button").click()
#
#     pas = browser.find_element(By.TAG_NAME, "password")
#     print(pas.text)
#
#
# finally:
#
#     browser.quit()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# with driver as driver:
#     driver.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
#     elements = driver.find_elements(By.CLASS_NAME, 'block')
#     for element in elements:
#         element.find_element(By.TAG_NAME, 'button').click()
#         print(element.find_element(By.TAG_NAME, 'button').text)
#     print(driver.find_element(By.TAG_NAME, 'password').text)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("https://parsinger.ru/selenium/3/3.3.2/index.html")
# blocks = browser.find_elements(By.CLASS_NAME, "block")
# for block in blocks:
#     button = block.find_element(By.TAG_NAME, "button")
#     button.click()
#     time.sleep(1)
# pswrd = browser.find_element(By.TAG_NAME, "password")
# print(pswrd.text)