from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")
    element = browser.find_element(By.ID, 'context-area')
    actions = ActionChains(browser)
    actions.context_click(element).perform()
    browser.find_element(By.CSS_SELECTOR, '[data-action="get_password"]').click()
    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
    time.sleep(5)
