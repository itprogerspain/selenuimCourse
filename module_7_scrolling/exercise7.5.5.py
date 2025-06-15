from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

with Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.7/1/index.html")
    buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for button in buttons:
        browser.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.1)
        button.click()
    time.sleep(1)
    print(browser.switch_to.alert.text)




# from selenium.webdriver import Chrome, ActionChains
#
# URL = "https://parsinger.ru/selenium/5.7/1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     uraniums = driver.find_elements("class name", "clickMe")
#     for uranium in uraniums:
#         action.scroll_to_element(uranium).perform()
#         uranium.click()
#     result = driver.switch_to.alert.text
#     print("Result is:", result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
#     for elem in browser.find_elements(By.CLASS_NAME, 'clickMe'):
#         elem.click()
#     print(browser.switch_to.alert.text)




# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
#
#     pieces = browser.find_elements(By.CSS_SELECTOR, 'button.clickMe')
#     for piece in pieces:
#         browser.execute_script(
#             'return arguments[0].scrollIntoView(true);', piece
#         )
#         piece.click()
#
#     alert = browser.switch_to.alert
#     result = alert.text
#     print(result)
#     alert.accept()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with (webdriver.Chrome() as browser):
#     browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
#     [button.click() for button in browser.find_elements(By.CSS_SELECTOR, '.clickMe')]
#     print(browser.switch_to.alert.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# URL = "https://parsinger.ru/selenium/5.7/1/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(URL)
#     data = driver.find_elements(By.CSS_SELECTOR, '.button-container .clickMe')
#     for button in data:
#         driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button)).click()
#
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     alert_text = driver.switch_to.alert.text
#     print(alert_text)