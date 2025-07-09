from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    wait = WebDriverWait(browser, 15)

    checkboxes = browser.find_elements(By.TAG_NAME, 'input')
    buttons = browser.find_elements(By.TAG_NAME, 'button')
    for checkbox, button in zip(checkboxes, buttons):
        if wait.until(EC.element_to_be_selected(checkbox)):
            button.click()

    print(wait.until(EC.visibility_of(browser.find_element(By.ID, 'result'))).text)



# GFD9-3SV0-3280-WEZC-23UN-Q921-3G5D




# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/5.9/7/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 30)
#     boxes = driver.find_elements("class name", "container")
#     for box in boxes:
#         checkbox = box.find_element("tag name", "input")
#         waiter.until(ec.element_to_be_selected(checkbox))
#         box.find_element("tag name", "button").click()
#     result = driver.find_element("id", "result").text
#     print("Result is:", result)




# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/7/index.html')
#
#     blocks = driver.find_elements(By.CLASS_NAME, 'container')
#
#     for block in blocks:
#         overlay = block.find_element(By.CLASS_NAME, 'overlay')
#
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="checkbox"]')))
#
#         WebDriverWait(driver, 10).until(EC.invisibility_of_element(overlay))
#
#         block.find_element(By.TAG_NAME, 'button').click()
#
#     result = driver.find_element(By.ID, 'result').text
#     print(result)