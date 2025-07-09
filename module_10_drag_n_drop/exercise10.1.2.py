from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    points = browser.find_elements(By.CLASS_NAME, "controlPoint")
    element = browser.find_element(By.ID, 'block1')

    actions.click_and_hold(element)
    for i in range(len(points)):
        actions.move_to_element(points[i])
    actions.perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# Ni44NTc4MTk2NzY4NTQ0NTZlKzIz




# import time
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/draganddrop/3/index.html')
#     time.sleep(1)
#     drag = browser.find_element(By.ID, 'block1')
#     actions = ActionChains(browser)
#     lst = [10] * 30
#     actions.click_and_hold(drag)
#     for x in lst:
#         actions.move_by_offset(x, 0)
#     actions.perform()
#     password = browser.find_element(By.ID, "message")
#     print(password.text)
#     time.sleep(2)




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# URL = "https://parsinger.ru/draganddrop/3/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     block = driver.find_element("id", "block1")
#     result = driver.find_element("id", "message").text
#     while not result:
#         action.drag_and_drop_by_offset(block, 10, 0).perform()
#         result = driver.find_element("id", "message").text
#     print("Result is:", result)



# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/draganddrop/3/index.html")
#     element_to_drag = browser.find_element(By.ID, "block1")
#     control_points = browser.find_elements(By.CLASS_NAME, 'controlPoint')
#     for control_point in control_points:
#         ActionChains(browser).drag_and_drop(element_to_drag, control_point).perform()
#     ActionChains(browser).move_by_offset(1, 0).perform()
#     print(browser.find_element(By.ID, "message").text)
#     #ime.sleep(100)





# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as condition
# from selenium.webdriver.support.ui import WebDriverWait
#
# if __name__ == '__main__':
#     url = 'https://parsinger.ru/draganddrop/3/index.html'
#
#     with webdriver.Chrome() as driver:
#         driver.get(url)
#         wait, action = WebDriverWait(driver, 60), ActionChains(driver)
#
#         draggable = driver.find_element(By.ID, 'block1')
#         for point in driver.find_elements(By.CLASS_NAME, 'controlPoint'):
#             action.drag_and_drop(draggable, point).perform()
#
#         print(wait.until(condition.visibility_of_element_located((By.ID, 'message'))).text)