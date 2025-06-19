from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    wait = WebDriverWait(browser, 30)
    browser.find_element(By.ID, 'startScan').click()
    wait.until(EC.title_is('Access Granted'))
    print(wait.until(
        EC.visibility_of_element_located((By.ID, 'passwordValue'))).text)




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.2.1/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("id", "startScan").click()
#     waiter = WebDriverWait(driver, 50, 0.5)
#     waiter.until(EC.title_is("Access Granted"))
#     result = driver.find_element("id", "passwordValue").text
#     print(result)


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.2.1/index.html")
#     browser.find_element(By.ID, "startScan").click()
#     WebDriverWait(browser, 30).until(EC.title_is("Access Granted"))
#     print(browser.find_element(By.ID, "passwordValue").text.split(": ")[1])