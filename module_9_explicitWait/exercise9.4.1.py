from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    wait = WebDriverWait(browser, 10)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn')
    buttons[-1].click()
    wait.until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'))
    print(wait.until(
        EC.visibility_of_element_located((By.ID, 'password'))).text)




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.4.3/index.html"
# url_template = "https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("css selector", ".btn:last-child").click()
#     waiter = WebDriverWait(driver, 20, 0.2)
#     waiter.until(EC.url_to_be(url_template))
#     result = driver.find_element("id", "password").text
#     print("Result is:", result)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
#     browser.find_element(By.LINK_TEXT, 'Правильный путь').click()
#     WebDriverWait(browser, timeout=6).until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'))
#     print(browser.find_element(By.ID, 'password').text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
#     browser.find_element(By.CSS_SELECTOR, 'body > div > a:nth-child(5)').click()
#     WebDriverWait(browser, 10).until(EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
#     print(browser.find_element(By.ID, 'password').text)



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
#     browser.get("https://parsinger.ru/selenium/9/9.4.3/index.html")
#     browser.find_elements(By.CLASS_NAME, "btn")[-1].click()
#     WebDriverWait(browser, 10).until(
#         EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure")
#     )
#     print(browser.find_element(By.ID, 'password').text)



# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
#
#     links = driver.find_elements(By.TAG_NAME, 'a')
#
#     for link in links:
#         if link.text == 'Правильный путь':
#             link.click()
#
#             WebDriverWait(driver, 10).until(
#                 EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure')
#             )
#
#             print(
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, 'password'))
#                 ).text
#             )
#
#     driver.quit()




# import time
#
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = "https://parsinger.ru/selenium/9/9.4.3/index.html"
# url_search = "https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     count = 0
#
#     while True:
#         buttons = driver.find_elements(By.CLASS_NAME, "btn")
#         buttons[count].click()
#         try:
#             WebDriverWait(driver, 10).until(EC.url_to_be(url_search))
#             password = driver.find_element(By.ID, "password")
#             print(password.text)
#             break
#         except TimeoutException:
#             driver.find_element(By.CLASS_NAME, "btn").click()
#             count += 1
#             time.sleep(1)