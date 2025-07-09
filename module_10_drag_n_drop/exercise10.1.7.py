from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    elements = browser.find_elements(By.CLASS_NAME, "piece")
    targets = browser.find_elements(By.CLASS_NAME, "range")
    for element, target in zip(elements, targets):
        actions.click_and_hold(element).move_to_element(target).release().perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# GD60-34JX-354F-3HJC-NXC0-54KO-W3B1-2DFH-23JG





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = 'https://parsinger.ru/selenium/5.10/8/index.html'
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#
#     # Ожидание загрузки страницы
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'content'))
#     )
#
#     for i in range(1, 9):  # Перебор всех piece и range с 1 до 8
#         piece_id = f'piece_{i}00'
#         range_id = f'range_{i}00'
#
#         piece_element = driver.find_element(By.ID, piece_id)
#         range_element = driver.find_element(By.ID, range_id)
#
#         # Получение расстояния из текста внутри тега <p> в range_
#         distance_text = range_element.find_element(By.TAG_NAME, 'p').text
#         distance = int(distance_text.split(': ')[1].replace('px', ''))
#
#         # Перемещение piece в range_ с помощью .move_by_offset()
#         action = ActionChains(driver)
#         action.drag_and_drop_by_offset(piece_element, distance, 0).perform()  # Обновлено смещение по оси x
#
#     # Ожидание появления сообщения
#     message = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'message'))
#     )
#
#     print(message.text)  # Вывод сообщения





# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# URL = "https://parsinger.ru/selenium/5.10/8/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     time.sleep(2)
#     pieces = driver.find_elements("class name", "piece")
#     fields = driver.find_elements("class name", "range")
#     for i in range(len(pieces)):
#         ActionChains(driver).drag_and_drop(pieces[i], fields[i]).perform()
#     print("Result is:", driver.find_element("id", "message").text)