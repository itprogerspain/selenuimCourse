from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
    wait = WebDriverWait(browser, 15)
    count = 0
    browser.find_element(By.ID, 'showProducts').click()
    try:
        prices = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'price')))
    except TimeoutException:
        print('TimeoutException_1')

    for price in prices:
        count += int(price.text.replace('$', ''))
    browser.find_element(By.ID, 'sumInput').send_keys(count)
    browser.find_element(By.ID, 'checkSum').click()
    try:
        print(wait.until(EC.visibility_of_element_located((By.ID, 'secretMessage'))).text)
    except TimeoutException:
        print('TimeoutException_2')





# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.5.3/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("id", "showProducts").click()
#     nums = [int(price.text.strip("$")) for price in WebDriverWait(driver, 25).until(ec.visibility_of_all_elements_located(("css selector", ".price")))]
#     driver.find_element("id", "sumInput").send_keys(sum(nums))
#     driver.find_element("id", "checkSum").click()
#     result = WebDriverWait(driver, 5).until(ec.visibility_of_element_located(("id",  "secretMessage"))).text
#     print("Result is:", result)




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
#     browser.get("https://parsinger.ru/selenium/9/9.5.3/index.html")
#     browser.find_element(By.ID, "showProducts").click()
#     WebDriverWait(browser, 20).until(
#         EC.visibility_of_all_elements_located((By.CLASS_NAME, "product"))
#     )
#
#     res = 0
#     for product in browser.find_elements(By.CLASS_NAME, "product"):
#         res += int(product.find_element(By.CLASS_NAME, "price").text.lstrip("$"))
#
#     browser.find_element(By.ID, "sumInput").send_keys(res)
#     browser.find_element(By.ID, "checkSum").click()
#     print(
#         WebDriverWait(browser, 5)
#         .until(EC.visibility_of_element_located((By.ID, "secretMessage")))
#         .text
#     )




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
#     browser.find_element(By.ID, 'showProducts').click()
#     locator = (By.CLASS_NAME, 'price')
#     products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(locator))
#     res = 0
#     for product in products:
#         res += int(product.text[1:])
#     browser.find_element(By.ID, 'sumInput').send_keys(res)
#     browser.find_element(By.ID, 'checkSum').click()
#     password = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'secretMessage')))
#     print(password.text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
#     browser.find_element(By.ID, 'showProducts').click()
#
#     locator = (By.CLASS_NAME, 'product')
#     WebDriverWait(browser, 60).until(EC.visibility_of_all_elements_located(locator))
#     out = [int(element.text.replace(',','')[1:]) for element in browser.find_elements(By.CLASS_NAME, 'price')]
#
#     browser.find_element(By.ID, 'sumInput').send_keys(sum(out))
#     browser.find_element(By.ID, 'checkSum').click()
#
#     print(WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'secretMessage'))).text)