from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.common.by import By
import time

with Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
    action = ActionChains(browser)
    action.send_keys(Keys.TAB).pause(0.2).perform()
    for _ in range(10):
        action.send_keys(Keys.END).pause(0.2).perform()

    action.send_keys(Keys.HOME).pause(0.2).perform()
    checkboxes = browser.find_elements(By.CLASS_NAME, 'child_container')
    for checkbox in checkboxes:
        inputs = checkbox.find_elements(By.TAG_NAME, 'input')
        for input_ in inputs:
            if int(input_.get_attribute('value')) % 2 == 0:
                input_.click()
    time.sleep(0.5)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    time.sleep(3)
    print(browser.switch_to.alert.text)



# from selenium.webdriver import Chrome, ActionChains, Keys
#
# URL = "https://parsinger.ru/selenium/5.7/4/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     action.send_keys(Keys.TAB).perform()
#     while True:
#         containers = driver.find_elements("class name", "child_container")
#         if len(containers) == 100:
#             action.send_keys(Keys.HOME).perform()
#             break
#         else:
#             action.send_keys(Keys.END).perform()
#     for container in containers:
#         checkboxes = container.find_elements("css selector", "input[type='checkbox']")
#         for checkbox in checkboxes:
#             if int(checkbox.get_attribute("value")) % 2 == 0:
#                 checkbox.click()
#     driver.find_element("class name", "alert_button").click()
#     result = driver.switch_to.alert.text
#     print("Result is:", result)



# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# url = 'https://parsinger.ru/selenium/5.7/4/index.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     actions = ActionChains(browser)
#     div = browser.find_element(By.ID, 'main_container')
#     for _ in range(100):
#         browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 100;", div)
#     time.sleep(2)
#     inputs = browser.find_elements(By.CSS_SELECTOR, 'div.child_container > input')
#     print(len(inputs))
#     for marker in inputs:
#         actions.move_to_element(marker).perform()
#         if int(marker.get_attribute('value')) % 2 == 0:
#             marker.click()
#     time.sleep(2)
#     alert_button = browser.find_element(By.CLASS_NAME, 'alert_button')
#     alert_button.click()
#     print(browser.switch_to.alert.text)



# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
#     browser.find_element(By.ID, 'main_container').click()
#     actions = ActionChains(browser)
#     for _ in range(100):
#         items = [x for x in browser.find_elements(By.CLASS_NAME, 'child_container')]
#         actions.key_down(Keys.CONTROL).key_down(Keys.END).perform()
#     for item in browser.find_elements(By.TAG_NAME, 'input'):
#         if int(item.get_attribute('value')) % 2 == 0:
#             item.click()
#     browser.find_element(By.CLASS_NAME, 'alert_button').click()
#     print(browser.switch_to.alert.text)



# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
#     actions = ActionChains(browser)
#     scroll=browser.find_element(By.ID,'main_container')
#     old = 0
#     while True:
#         scroll.send_keys(Keys.END)
#         time.sleep(0.5)
#         new = len(browser.find_elements(By.CSS_SELECTOR, '.child_container'))
#         if new==old:
#             break
#         old = new
#
#     all_check = browser.find_elements(By.CSS_SELECTOR, ".child_container")
#     for check in all_check:
#         check = check.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
#         for i in check:
#             if int(i.get_attribute("value"))%2==0:
#                 i.click()
#
#     browser.find_element(By.CSS_SELECTOR, ".alert_button").click()
#     time.sleep(1)
#     print(browser.switch_to.alert.text)

