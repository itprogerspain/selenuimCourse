from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")


with webdriver.Chrome() as browser:
    browser.get('https://bot.sannysoft.com/')
    browser.execute_script("Object.defineProperty(Navigator.prototype, 'webdriver', {value: false});")
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    # actions = ActionChains(browser)
    # time.sleep(60)
    print(browser.execute_script("return navigator.webdriver"))

