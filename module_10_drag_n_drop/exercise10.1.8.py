from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    sliders = browser.find_elements(By.CLASS_NAME, "volume-slider")
    targets = browser.find_elements(By.CLASS_NAME, "target-value")

    for slider, target in zip(sliders, targets):
        current_value = int(slider.get_attribute("value"))
        target_value = int(target.text)
        if int(target.text) > current_value:
            for _ in range(int(target.text) - current_value):
                slider.send_keys(Keys.ARROW_RIGHT)
        else:
            for _ in range(current_value - int(target.text)):
                slider.send_keys(Keys.ARROW_LEFT)
        time.sleep(0.1)
    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# 3F9D-DVB0-EH46-96VB-JHJ5-34UK-2SSF-JKG0




# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Используйте контекстный менеджер для автоматического закрытия браузера
# with webdriver.Chrome() as driver:
#     # Перейти на сайт
#     driver.get("https://parsinger.ru/selenium/5.10/6/index.html")
#
#     # Получить список всех контейнеров слайдеров
#     slider_containers = driver.find_elements(By.CLASS_NAME, "slider-container")
#
#     for container in slider_containers:
#         # Найти слайдер внутри контейнера
#         slider = container.find_element(By.CLASS_NAME, "volume-slider")
#
#         # Получить текущее и целевое значение слайдера
#         current_value = int(slider.get_attribute("value"))
#         target_value = int(container.find_element(By.CLASS_NAME, "target-value").text)
#
#         # Передвигаем слайдер к целевому значению
#         while current_value != target_value:
#             if current_value < target_value:
#                 # Увеличиваем значение
#                 slider.send_keys(Keys.ARROW_RIGHT)
#                 current_value += 1
#             else:
#                 # Уменьшаем значение
#                 slider.send_keys(Keys.ARROW_LEFT)
#                 current_value -= 1
#
#     # Ожидаем появления сообщения в теге <p id="message"></p>
#     message_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "message"))
#     )
#
#     # Копируем сообщение
#     message = message_element.text
#     print("Сообщение:", message)




# from selenium import webdriver
# #from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
#
# URL = "https://parsinger.ru/selenium/5.10/6/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     time.sleep(2)
#     containers = driver.find_elements("class name", "slider-container")
#     for container in containers:
#         left = int(container.find_element("class name", "current-value").text)
#         right = int(container.find_element("class name", "target-value").text)
#         slider = container.find_element("class name", "volume-slider")
#         if left > right:
#             button = Keys.LEFT
#         else:
#             button = Keys.RIGHT
#         for _ in range(abs(left - right)):
#             slider.send_keys(button)
#     print("Result is:", driver.find_element("id", "message").text)