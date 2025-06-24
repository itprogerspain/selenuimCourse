from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
    wait = WebDriverWait(browser, 15)
    try:
        element = wait.until(EC.visibility_of_element_located((By.ID, 'order-number')))
        print(element.text)

    except TimeoutException:
        time.sleep(2)
        browser.refresh()
        element = wait.until(EC.visibility_of_element_located((By.ID, 'order-number')))
        print(element.text)


# TR07NGM19XTR07NGM19X




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.5.1/index.html")
#     print(WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'order-number'))).text)
#


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.5.1/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 20)
#     code = ("id", "order-number")
#     result = waiter.until(ec.presence_of_element_located(code)).text
#     print("Result is:", result)




import time
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
#
#     try:
#         element = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, 'order-number'))
#         )
#         print(element.text)
#     except TimeoutException:
#         print("Элемент не появился за 20 секунд")




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
#     locator = (By.ID, 'order-number')
#     WebDriverWait(browser, timeout=10).until(EC.presence_of_element_located(locator))
#     print(browser.find_element(*locator).text)