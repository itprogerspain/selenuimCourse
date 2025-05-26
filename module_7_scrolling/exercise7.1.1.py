import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    height = browser.execute_script('return document.body.scrollHeight')
    browser.execute_script(f'window.scrollBy(0, {height})')
    time.sleep(3)
    print(browser.find_element(By.ID, 'secret-container').text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
#
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/7/7.1/index.html')
#
#     # получить высоту окна
#     height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script(f"window.scrollBy(0, {height})")
#
#     WebDriverWait(driver, 5).until(text_to_be_present_in_element((By.ID, 'secret-container'), "Пароль"))
#
#     print(driver.find_element(By.ID, 'secret-container').text)





# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
#
#     page_height = browser.execute_script('return document.body.scrollHeight')
#     browser.execute_script(f'window.scrollTo(0, {page_height})')
#
#     password = browser.find_element(By.CSS_SELECTOR, '#secret-container')
#     WebDriverWait(browser, 5).until(lambda _: password.text.strip() != '')
#     print(password.text.split()[1].strip())