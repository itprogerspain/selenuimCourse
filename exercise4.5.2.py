import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)




# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/2/2.html')
#     browser.find_element(By.LINK_TEXT, '16243162441624').click()
#     result = browser.find_element(By.CSS_SELECTOR, '#result').text
#     print(result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/selenium/2/2.html"
# text = 16243162441624
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     driver.find_element(By.XPATH, f"//a[text()='{text}']").click()
#     res = driver.find_element(By.CSS_SELECTOR, "p#result").text
#     print(res)