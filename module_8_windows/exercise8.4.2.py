from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
    frames = ['frame1', 'frame2', 'frame3']
    for frame in frames:
        browser.switch_to.frame(browser.find_element(By.ID, frame))
        browser.find_element(By.CLASS_NAME, 'unlock-button').click()
        browser.switch_to.default_content()

    browser.switch_to.frame(browser.find_element(By.ID, 'frame4'))
    print(browser.find_element(By.TAG_NAME, 'h2').text)



# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
#     i = 1
#     while True:
#         try:
#             iframe = browser.find_element(By. ID, f"frame{i}")
#             browser.switch_to.frame(iframe)
#             password = browser.find_element(By.TAG_NAME, 'h2')
#             print(password.text)
#             break
#         except:
#             browser.find_element(By.CLASS_NAME, 'unlock-button').click()
#             browser.switch_to.default_content()
#             i += 1




# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/selenium/8/8.4.2/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     for i in range(1, 5):
#         iframe = driver.find_element("id", f"frame{i}")
#         driver.switch_to.frame(iframe)
#         if i != 4:
#             driver.find_element("class name", "unlock-button").click()
#         else:
#             result = driver.find_element("tag name", "h2").text
#             print(result)
#         driver.switch_to.default_content()




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     url = "https://parsinger.ru/selenium/8/8.4.2/index.html"
#     browser.get(url)
#
#     for i in range(3):
#         browser.switch_to.frame(i)
#         time.sleep(1)
#         browser.find_element(By.TAG_NAME, 'button').click()
#         browser.switch_to.default_content()
#
#     browser.switch_to.frame(3)
#     print(browser.find_element(By.TAG_NAME, 'h2').text)
#     browser.switch_to.default_content()
#



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
#     browser.switch_to.frame(browser.find_element(By.ID, 'frame1'))
#     browser.find_element(By.CLASS_NAME, 'unlock-button').click()
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.find_element(By.ID, 'frame2'))
#     browser.find_element(By.CLASS_NAME, 'unlock-button').click()
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.find_element(By.ID, 'frame3'))
#     browser.find_element(By.CLASS_NAME, 'unlock-button').click()
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.find_element(By.ID, 'frame4'))
#     print(browser.find_element(By.TAG_NAME, 'h2').text)





# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
#
#     for i in range(1, 5):
#         iframe = browser.find_element(By.CSS_SELECTOR, f'iframe#frame{i}')
#         browser.execute_script(
#             'return arguments[0].scrollIntoView(true);', iframe
#         )
#         browser.switch_to.frame(iframe)
#         if i != 4:
#             browser.find_element(
#                 By.CSS_SELECTOR, 'button.unlock-button'
#             ).click()
#             browser.switch_to.default_content()
#         else:
#             password = browser.find_element(By.CSS_SELECTOR, 'h2')
#             print(password.text.rsplit(' ', 1)[1].strip())