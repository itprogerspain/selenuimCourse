from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    element = browser.find_element(By.ID, "draggable")
    targets = browser.find_elements(By.CLASS_NAME, "box")
    for target in targets:
        actions.click_and_hold(element).move_to_element(target).release().perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)




# NS4zNDUzMzU0NTQ2MzU0NDVlKzI



# import time
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/draganddrop/2/index.html')
#     time.sleep(1)
#     drag = browser.find_element(By.ID, 'draggable')
#     actions = ActionChains(browser)
#     bloks = browser.find_elements(By.CLASS_NAME, "box")
#     for x in bloks:
#         actions.drag_and_drop(drag, x).perform()
#     print(browser.find_element(By.ID, 'message').text)



# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = "https://parsinger.ru/draganddrop/2/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     circle = driver.find_element("id", "draggable")
#     for box in driver.find_elements("class name", "box"):
#         action.drag_and_drop(circle, box).perform()
#     print("Result is:", driver.find_element("id", "message").text)