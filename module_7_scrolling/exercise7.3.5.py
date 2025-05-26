from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
    element1 = browser.find_element(By.ID, 'scrollable-container-left')
    element2 = browser.find_element(By.ID, 'scrollable-container-right')
    actions = ActionChains(browser)
    actions.move_to_element(element1).click(element1).send_keys(Keys.END).perform()
    time.sleep(0.2)
    actions.move_to_element(element2).click(element2).send_keys(Keys.END).perform()
    time.sleep(0.2)
    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
    time.sleep(5)






# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
#     wait = WebDriverWait(browser, 10)
#     actions = ActionChains(browser)
#     containers = browser.find_elements(By.CSS_SELECTOR, "[id*='scrollable-container']")
#     for container in containers:
#         actions.send_keys_to_element(container, Keys.END).perform()
#     res = wait.until(
#         ec.visibility_of_element_located((By.CSS_SELECTOR, "[key='access_code']"))
#     )
#     print(res.text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
# browser = webdriver.Chrome()
# browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
# actions = ActionChains(browser)
# scroll_containers = browser.find_elements(By.CLASS_NAME, "scroll-container")
# for scroll in scroll_containers:
#     scroll.click()
#     actions.send_keys(Keys.END).perform()
# time.sleep(2)
# print(browser.find_element(By.CSS_SELECTOR, "[key='access_code']").text)
# browser.quit()




# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/7/7.3.5/index.html')
#     scrollable_container_left = driver.find_element(By.ID, 'scrollable-container-left')
#     scrollable_container_right = driver.find_element(By.ID, 'scrollable-container-right')
#
#     actions = ActionChains(driver)
#     actions.key_down(Keys.END, scrollable_container_left)\
#         .key_down(Keys.END, scrollable_container_right)\
#         .perform()
#
#     actions.key_up(Keys.END, scrollable_container_left)\
#         .key_up(Keys.END, scrollable_container_right)\
#         .perform()
#
#     print(
#         WebDriverWait(driver, 3).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[key="access_code"]'))
#         ).text
#     )





# from selenium.webdriver import Chrome, ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# with Chrome() as browser:
#     action = ActionChains(browser)
#     browser.get('https://parsinger.ru/selenium/7/7.3.5/index.html')
#     elem1 = browser.find_element(By.ID, 'scrollable-container-right')
#     elem2 = browser.find_element(By.ID, 'scrollable-container-left')
#     action.send_keys_to_element(elem1, Keys.END).send_keys_to_element(
#         elem2, Keys.END).pause(1).perform()
#     print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)