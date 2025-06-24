from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')
    wait = WebDriverWait(browser, 15)
    count = 0
    browser.find_element(By.ID, 'startButton').click()
    last_url = ''
    try:
        while True:
            wait.until(lambda b: b.current_url != last_url)
            last_url = browser.current_url
            if EC.url_matches(r"^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$")(browser):
                count += int(browser.find_element(By.CLASS_NAME, 'number').text)
    except TimeoutException:
        print(count)
        browser.find_element(By.ID, 'sumInput').send_keys(count)
        browser.find_element(By.ID, 'checkButton').click()
        print(browser.find_element(By.ID, 'result').text)


# AbcD123XyZ