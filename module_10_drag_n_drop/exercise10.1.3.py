from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    elements = browser.find_elements(By.CLASS_NAME, "draganddrop")
    for element in elements:
        actions.click_and_hold(element)
        actions.move_by_offset(700, 0)
        actions.release().perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# Ni44NTc4MTk2NzY4NTQ0NTZlKzIz



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# url = "https://parsinger.ru/selenium/5.10/2/index.html"
#
# with webdriver.Chrome() as driver:
#     # Переходим на сайт
#     driver.get(url)
#
#     # Ожидаем загрузки страницы (в реальном коде лучше использовать WebDriverWait)
#     time.sleep(2)
#
#     # Находим все элементы, которые нужно перетащить
#     draggable_elements = driver.find_elements(By.CLASS_NAME, "draganddrop")
#
#     # Находим целевой элемент (серую зону)
#     target_element = driver.find_element(By.CLASS_NAME, "draganddrop_end")
#
#     # Инициализируем объект ActionChains
#     actions = ActionChains(driver)
#
#     # Перетаскиваем каждый элемент
#     for draggable in draggable_elements:
#         actions.drag_and_drop(draggable, target_element).perform()
#         # Ожидаем завершения анимации перетаскивания (в реальном коде лучше использовать WebDriverWait)
#         time.sleep(1)
#
#     # Получаем и выводим сообщение
#     message = driver.find_element(By.ID, "message").text
#     print("Сообщение:", message)





# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
#
#     container = browser.find_element(By.CLASS_NAME, 'draganddrop_end')
#     action = ActionChains(browser)
#
#     for i in range(1, 11):
#         element = browser.find_element('id', f'draganddrop{i}')
#         action.drag_and_drop(element, container).perform()
#         time.sleep(0.5)
#
#     pswrd = WebDriverWait(browser, 5).until(EC.presence_of_element_located(('id', 'message')))
#     print(pswrd.text)





# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# URL = "https://parsinger.ru/selenium/5.10/2/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     time.sleep(5)
#     for block in driver.find_elements("class name", "draganddrop"):
#         action.drag_and_drop(block, driver.find_element("class name", "draganddrop_end")).perform()
#     print("Result is:", driver.find_element("id", "message").text)