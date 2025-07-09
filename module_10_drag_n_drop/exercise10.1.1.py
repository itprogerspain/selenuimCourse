from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get("https://parsinger.ru/draganddrop/1/index.html")
    time.sleep(1)
    element = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "field2")
    actions = ActionChains(driver)
    # actions.drag_and_drop(element, target).perform()
    actions.click_and_hold(element).move_to_element(target).release().perform()
    print(driver.find_element(By.ID, 'result').text)



# ODYzNDQ1MzM0NTE0MzQ2OTAwMA==



# import time
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/draganddrop/1/index.html')
#     time.sleep(3)
#     drag = browser.find_element(By.XPATH, '//*[@id="draggable"]')
#     final = browser.find_element(By.XPATH, '//*[@id="field2"]')
#     actions = ActionChains(browser)
#
#     actions.drag_and_drop(drag, final).perform()
#     result = browser.find_element(By.ID, 'result').text
#     print(result)



# with webdriver.Chrome() as browser:
#     browser.get(url)
#     actions = ActionChains(browser)
#     wait = WebDriverWait(browser, 90, 0.5)
#     item = browser.find_element(By.XPATH, '//div[@id="draggable"]')
#     field = browser.find_element(By.XPATH, '//div[@id="field2"]')
#     actions.drag_and_drop(item, field).perform()
#     answer = browser.find_element(By.XPATH, '//div[@id="result"]').text
#     print(answer)




