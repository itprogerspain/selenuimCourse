import time
from selenium import webdriver
from selenium.webdriver.common.by import By


proxy = '8.210.83.33:80'
url = 'https://whoer.net/es'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, 'fc-button-label').click()
    print(browser.find_element(By.CSS_SELECTOR, '.your-ip strong').text)
    time.sleep(5)


