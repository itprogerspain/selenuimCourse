from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

    for i in range(4):
        browser.switch_to.frame(browser.find_element(By.TAG_NAME, 'iframe'))
        browser.find_element(By.CLASS_NAME, 'button').click()
    print(browser.find_element(By.CLASS_NAME, 'password-container').text)


    # IM-IFRAME-N1NJ4




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--window-size=1920,1080')
#
# with webdriver.Chrome(options=chrome_options) as driver:
#     wait = WebDriverWait(driver, 2, .5)
#     driver.get('https://parsinger.ru/selenium/8/8.4.3/index.html')
#
#     while True:
#         try:
#             driver.switch_to.frame(wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe'))))
#             driver.find_element(By.TAG_NAME, 'button').click()
#         except:
#             print(driver.find_element(By.CLASS_NAME, 'password-container').text)
#             break



# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')
#     while True:
#             iframe = browser.find_element(By.TAG_NAME, "iframe")
#             browser.switch_to.frame(iframe)
#             browser.find_element(By.CLASS_NAME, 'button').click()
#             pass_elements = browser.find_elements(By.CLASS_NAME, 'password-container')
#             if len(pass_elements) > 0:
#                 password = browser.find_element(By.CLASS_NAME, 'password-container')
#                 print(password.text)
#                 break
