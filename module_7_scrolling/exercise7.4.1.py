from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
    header_ = browser.find_element(By.CSS_SELECTOR, 'header')
    action = ActionChains(browser)
    # for x in range(3):
    #     action.move_to_element(header_).scroll_by_amount(1, 600).perform()
    action.move_to_element(header_).scroll_by_amount(1, 800).perform()
    time.sleep(5)

    marker_1 = browser.find_element(By.CLASS_NAME, 'marker-1')
    action.move_to_element(marker_1).scroll_by_amount(1, 800).perform()
    code = browser.find_element(By.CLASS_NAME, 'countdown').text.split(' ')[-1]
    browser.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(code)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    print(browser.find_element(By.ID, 'final-key').text)




# from selenium.webdriver import Chrome, ActionChains
#
#
# URL = "https://parsinger.ru/selenium/7/7.4.1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     target = driver.find_element("class name", "long-page")
#     action.move_to_element(target).scroll_by_amount(0, 800).pause(3).perform()
#     code = driver.find_element("class name", "countdown").text.split(": ")[-1]
#     action.scroll_by_amount(0, 1000).pause(2).perform()
#     driver.find_element("css selector", ".step-content input").send_keys(code)
#     driver.find_element("css selector", ".step-content button").click()
#     result = driver.find_element("id", "final-key").text
#     print(result)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get(r"https://parsinger.ru/selenium/7/7.4.1/index.html")
#     ActionChains(browser).scroll_by_amount(0, 2000).perform()
#     time.sleep(4)
#     password = browser.find_element(By.CLASS_NAME, 'countdown').text[5:]
#     browser.find_element(By.TAG_NAME, 'input').send_keys(password)
#     browser.find_element(By.TAG_NAME, 'button').click()
#     print(browser.find_element(By.ID, 'final-key').text)
