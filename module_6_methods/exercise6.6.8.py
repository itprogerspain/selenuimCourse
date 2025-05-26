import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    elements = browser.find_elements(By.CLASS_NAME, "parent")
    for element in elements:
        gray = element.find_element(By.CSS_SELECTOR, "textarea[color='gray']")
        blue = element.find_element(By.CSS_SELECTOR, "textarea[color='blue']")
        blue.send_keys(gray.text)
        gray.clear()
        element.find_element(By.CSS_SELECTOR, "button").click()
    browser.find_element(By.ID, "checkAll").click()
    print(browser.find_element(By.ID, "congrats").text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# url = 'https://parsinger.ru/selenium/5.5/4/1.html'
#
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     bloks = browser.find_elements(By.CLASS_NAME, 'parent')
#     for element in bloks:
#         value = element.find_element(By.XPATH, './textarea[1]').text
#         element.find_element(By.XPATH, './textarea[1]').clear()
#         element.find_element(By.XPATH, './textarea[2]').send_keys(value)
#         element.find_element(By.XPATH, './button').click()
#     browser.find_element(By.ID, 'checkAll').click()
#     print(browser.find_element(By.ID, 'congrats').text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/selenium/5.5/4/1.html"
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     elements = browser.find_elements(By.CLASS_NAME, "parent")
#     for element in elements:
#         text = element.find_element(By.CSS_SELECTOR, "textarea:nth-child(1)").text
#         element.find_element(By.CSS_SELECTOR, 'textarea:nth-child(2)').send_keys(f"{text}")
#         element.find_element(By.CSS_SELECTOR, "textarea:nth-child(1)").clear()
#         element.find_element(By.TAG_NAME, "button").click()
#     browser.find_element(By.ID, "checkAll").click()
#     print(browser.find_element(By.ID, "congrats").text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# URL = 'https://parsinger.ru/selenium/5.5/4/1.html'
#
# with webdriver.Chrome() as driver:
#     driver.get(URL)
#
#     parent_divs = driver.find_elements(By.CLASS_NAME, 'parent')
#
#     for div in parent_divs:
#         gray_textarea = div.find_element(By.XPATH, './textarea[@color="gray"]')
#         number = gray_textarea.get_attribute('value')
#         gray_textarea.clear()
#
#         blue_textarea = div.find_element(By.XPATH, './textarea[@color="blue"]')
#         blue_textarea.send_keys(number)
#
#         driver.execute_script("arguments[0].scrollIntoView();", blue_textarea)
#
#         button = div.find_element(By.TAG_NAME, 'button')
#
#         driver.implicitly_wait(1)
#
#         button.click()
#
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
#
#     check_all_btn = driver.find_element(By.ID, 'checkAll')
#     check_all_btn.click()
#
#     print(driver.find_element(By.ID, 'congrats').text)