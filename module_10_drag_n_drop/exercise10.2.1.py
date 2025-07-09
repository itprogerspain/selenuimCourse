from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
url = 'https://parsinger.ru/selenium/stealth/1/index.html'

with (
    webdriver.Chrome() as browser,
    webdriver.Chrome(options) as musked_browser
):

    browser.get(url)
    musked_browser.get(url)
    wait = WebDriverWait(musked_browser, 15)

    code = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "verification-code"))).text
    print(code)

    wait.until(EC.visibility_of_element_located((By.ID, "verification-input"))).send_keys(code)
    wait.until(EC.visibility_of_element_located((By.ID, "check-button"))).click()

    wait.until(lambda driver: musked_browser.find_element(By.ID, 'secret').text.strip() != '')
    secret_word = wait.until(EC.visibility_of_element_located((By.ID, "secret"))).text
    print(secret_word)


# SEL-BAM883
# Web1-Driver-Masked-0000




# from selenium import webdriver
# import time
#
# URL = "https://parsinger.ru/selenium/stealth/1/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     code = driver.find_element("id", "verification-code").text
#     time.sleep(1)
#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
#                             {"source": "Object.defineProperty(navigator, 'webdriver', {value: false});"})
#     driver.refresh()
#     driver.find_element("id", "verification-input").send_keys(code)
#     driver.find_element("id", "check-button").click()
#     result = driver.find_element("id", "secret").text
#     print(result)




from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/stealth/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    password = browser.find_element(By.ID, 'verification-code').text

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.find_element(By.ID, 'verification-input').send_keys(password)
    browser.find_element(By.ID, 'check-button').click()
    print(browser.find_element(By.ID, 'secret').text)