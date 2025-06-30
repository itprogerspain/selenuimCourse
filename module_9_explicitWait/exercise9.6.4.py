from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')

    wait = WebDriverWait(browser, 20)
    element = (By.ID, 'booking-number')
    password = (By.ID, 'secret-password')
    atribute_name = 'confirmed'

    try:
        wait.until(EC.element_attribute_to_include(element, atribute_name))
    except TimeoutException:
        print('TimeoutException_1')

    number = browser.find_element(*element).text
    browser.find_element(By.ID, 'booking-input').send_keys(number)
    browser.find_element(By.ID, 'check-button').click()

    try:
        print(wait.until(EC.visibility_of_element_located(password)).text)
    except TimeoutException:
        print('TimeoutException_2')

# SELENIUM_WAIT_MASTER


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# URL = "https://parsinger.ru/selenium/9/9.6.4/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 30)
#     booking = ("id", "booking-number")
#     try:
#         waiter.until(ec.element_attribute_to_include(booking, "confirmed"))
#         code = driver.find_element(*booking).text
#         driver.find_element("id", "booking-input").send_keys(code)
#         driver.find_element("id", "check-button").click()
#         result = driver.find_element("css selector", ".password-value").text
#         print("Result is:", result)
#     except:
#         print("Try again!")




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
#     browser.get("https://parsinger.ru/selenium/9/9.6.4/index.html")
#     WebDriverWait(browser, 30).until(
#         EC.element_attribute_to_include((By.ID, "booking-number"), "confirmed")
#     )
#     browser.find_element(By.ID, "booking-input").send_keys(
#         browser.find_element(By.ID, "booking-number").text
#     )
#     browser.find_element(By.ID, "check-button").click()
#
#     print(
#         WebDriverWait(browser, 10)
#         .until(EC.visibility_of_element_located((By.ID, "secret-password")))
#         .text
#     )