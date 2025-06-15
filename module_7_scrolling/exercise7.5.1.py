from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    items = browser.find_elements(By.CLASS_NAME, 'item')
    count = 0

    for item in items:
        box = item.find_element(By.CLASS_NAME, 'checkbox_class')
        box.click()
        time.sleep(0.3)

        span = item.find_element(By.CSS_SELECTOR, 'span')
        if span:
            text = span.text.strip()
            if text.isdigit():
                count += int(text)

    print(count)




# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
#
#
# URL = "https://parsinger.ru/scroll/2/index.html"
# result = []
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     for i in range(1, 101):
#         checkbox = driver.find_element("id", i)
#         action.send_keys(Keys.TAB).move_to_element(checkbox).click().perform()
#         num = driver.find_element("id", f"result{i}").text
#         if num:
#             result.append(int(num))
#     print("Result is:", sum(result))




# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# result = []
# with webdriver.Chrome() as browser:
#         browser.get('http://parsinger.ru/scroll/2/')
#
#         for tag_input in browser.find_elements(By.TAG_NAME, 'input'):
#             tag_input.send_keys(Keys.DOWN)
#             tag_input.click()
#
#         for x in browser.find_elements(By.TAG_NAME, 'span'):
#             if x.text.isdigit():
#                 result.append(int(x.text))
# print(sum(result))




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/scroll/2/index.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     checkboxes = browser.find_elements(By.CLASS_NAME, "checkbox_class")
#
#     total = 0
#     for i, checkbox in enumerate(checkboxes, start=1):
#         checkbox.click()
#         number = browser.find_element(By.ID, f"result{i}").text
#         total += int(number) if number else 0
#
#     print(total)