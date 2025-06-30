from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')
    wait = WebDriverWait(browser, 15)
    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'ghost-button'))).click()
        password = wait.until(EC.visibility_of_element_located((By.ID, 'password-display')))
        print(password.text)
    except TimeoutException:
        print('TimeoutException')



# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# URL = "https://parsinger.ru/selenium/9/9.5.2/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     WebDriverWait(driver, 10).until(ec.visibility_of_element_located(("id", "ghost-button"))).click()
#     result = driver.find_element("id", "password-display").text
#     print(result)




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
#     browser.get("https://parsinger.ru/selenium/9/9.5.2/index.html")
#     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'ghost-button'))).click()
#     print(browser.find_element(By.ID, 'password-display').text.split(': ')[1])



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')
#     locator = (By.ID, "ghost-button")
#     element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator)).click()
#     print(browser.find_element(By.ID,'password-display').text)

