from selenium.webdriver import Chrome, ActionChains, Keys

with Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.7/5/index.html")
    action = ActionChains(browser)
    buttons = browser.find_elements("class name", "timer_button")

    for i, button in enumerate(buttons):
        hold_time = button.get_attribute('value')
        action.click_and_hold(button).pause(float(hold_time)).release(button).perform()
        if i > len(buttons) - 1:
            ActionChains(browser).send_keys(Keys.TAB).perform()
    print(browser.switch_to.alert.text)


# GFL4-ED40-F32F-HJ24-0BXS-235N-PIRE-123VD-123F



# from selenium.webdriver import Chrome, ActionChains
#
#
# URL = "https://parsinger.ru/selenium/5.7/5/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     buttons = driver.find_elements("class name", "timer_button")
#     for button in buttons:
#         hold_time = float(button.get_attribute("value"))
#         action.click_and_hold(button).pause(hold_time).release(button).perform()
#     result = driver.switch_to.alert.text
#     print("Result is:", result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import pyperclip
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
#     actions = ActionChains(browser)
#     [actions.click_and_hold(button).pause(float(button.text)).release(button).perform() for button in browser.find_elements(By.XPATH, '//button')]
#     pyperclip.copy(browser.switch_to.alert.text)




# from selenium.webdriver import Chrome, ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# with Chrome() as browser:
#     action = ActionChains(browser)
#     browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
#     buttons = browser.find_elements(By.TAG_NAME, 'button')
#
#     for button in buttons:
#         sec = float(button.get_attribute('value'))
#         action.click_and_hold(button).pause(sec).perform()
#     time.sleep(20)




from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    elements = browser.find_elements(By.CLASS_NAME,"timer_button")
    actions = ActionChains(browser)
    for elem in elements:
        hold_time = float(elem.text) + 0.1
        actions.click_and_hold(elem).pause(hold_time).release(elem).perform()
    print(browser.switch_to.alert.text)



