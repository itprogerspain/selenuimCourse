from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")
    element = browser.find_element(By.ID, 'instructions')
    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL, element) \
        .key_down(Keys.ALT) \
        .key_down(Keys.SHIFT) \
        .key_down('T') \
        .key_up(Keys.CONTROL, element) \
        .key_up(Keys.ALT) \
        .key_up(Keys.SHIFT) \
        .key_up('T') \
        .perform()
    print(browser.find_element(By.TAG_NAME, "span").text)
    time.sleep(5)

    # print(browser.find_element(By.CSS_SELECTOR, 'span[key=access_code]').text)
    # print(browser.find_element(By.CSS_SELECTOR, 'p span').text)
    # print(browser.find_element(By.CSS_SELECTOR, "[key='access_code']").text)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# with webdriver.Chrome() as browser:
#     url = "https://parsinger.ru/selenium/7/7.3.3/index.html"
#     browser.get(url)
#     actions = ActionChains(browser)
#     actions.key_down(Keys.CONTROL) \
#     .key_down(Keys.ALT) \
#     .key_down(Keys.SHIFT) \
#     .send_keys("T") \
#     .key_up(Keys.SHIFT) \
#     .key_up(Keys.ALT) \
#     .key_up(Keys.CONTROL) \
#     .perform()
#     time.sleep(1)
#     key = browser.find_element(By.CSS_SELECTOR, "[key='access_code']").text
#     print(key)




from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.3/index.html')
    ActionChains(browser).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).key_up('T').perform()
    print(browser.find_element(By.CSS_SELECTOR, 'p span').text)