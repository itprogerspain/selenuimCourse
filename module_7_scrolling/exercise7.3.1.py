#  Решение от Ильи Мирошниченко


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/7/7.3.1/index.html")
    draggable = browser.find_element(By.ID, "draggable")
    actions = ActionChains(browser)
    actions.drag_and_drop_by_offset(draggable, 0, -210).perform()
    print(browser.find_element(By.ID, "password").text)



# # то же самое что и выше но упрощено в одну строку
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.3.1/index.html')
#     ActionChains(browser).drag_and_drop_by_offset(browser.find_element(By.ID, 'draggable'), 0, -200).perform()
#     print(browser.find_element(By.ID, 'password').text)





# # первоначальный код для понимания и разбора откуда и как взять координаты
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.3.1/index.html')
#
#     draggable = browser.find_element(By.ID, "draggable")
#     target = browser.find_element(By.ID, "target")
#
#     actions = ActionChains(browser)
#
#     draggable_location = draggable.location # координаты верхнего левого угла элемента
#     draggable_size = draggable.size # размеры элемента
#
#     target_location = target.location # координаты верхнего левого угла цели
#     target_size = target.size # размеры цели
#
#     x_offset = target_location['x'] - draggable_location['x'] # разница смещения углов цели и элемента
#     y_offset = target_location['y'] - draggable_location['y'] # разница смещения углов цели и элемента
#
#     # поиск  координат центров цели и елемента
#     drag_center_x = draggable_location['x'] + draggable_size['width'] // 2
#     drag_center_y = draggable_location['y'] + draggable_size['height'] // 2
#     target_center_x = target_location['x'] + target_size['width'] // 2
#     target_center_y = target_location['y'] + target_size['height'] // 2
#
#     # Смещение по центру
#     offset_x = target_center_x - drag_center_x
#     offset_y = target_center_y - drag_center_y
#
#     print(f"Смещение по X: {offset_x}, по Y: {offset_y}")
#
#     print(f"Координаты элемента: {draggable_location}")
#     print(f"Размер элемента: {draggable_size}")
#
#     print(f"Координаты целевой зоны: {target_location}")
#     print(f"Размер целевой зоны: {target_size}")
#
#     print('Смещение по Х:', x_offset)
#     print('Смещение по y:', y_offset)
#
#     actions.drag_and_drop_by_offset(draggable, 0, -209).perform()
#     print(browser.find_element(By.ID, "password").text)
#     time.sleep(5)



# import time
# from tqdm import tqdm
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# url = r'https://parsinger.ru/selenium/7/7.3.1/index.html'
#
# # Создание объекта ChromeOptions
# options_chrome = webdriver.ChromeOptions()
#
# # Добавление аргументов командной строки
# options_chrome.add_argument("--headless=new")  # фоновый режим работы
# options_chrome.add_argument('--disable-client-side-phishing-detection')  # Отключает обнаружение фишинга на клиентской стороне
# options_chrome.add_argument('--disable-cache')  # Отключает кэш браузера
#
# # Инициализация драйвера Chrome с указанными опциями
# # with webdriver.Chrome(options=options_chrome) as browser:  # фоновый режим
# with webdriver.Chrome() as browser:  # интерактивный режим
#     browser.get(url)
#     time.sleep(1)
#
#     # Использование ActionChains для выполнения перетаскивания элемента
#     actions = ActionChains(browser)
#
#     # Найти исходный и целевой элементы на странице с использованием локаторов By
#     source = browser.find_element(By.ID, "draggable")
#     target = browser.find_element(By.ID, "target")
#     actions.drag_and_drop(source, target).perform()
#     time.sleep(1)
#     password = browser.find_element(By.ID, "password").text
#     print(password)
#
# '''
# 1-@M-THE-GR34T-@ND-T3RR1BL3-P3T3R-GR1FF1N
# '''



#
#
# from selenium.webdriver import Chrome, ActionChains
# from selenium.webdriver.common.by import By
#
# with Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/7/7.3.1/index.html')
#     obj = browser.find_element(By.ID, 'draggable')
#     target = browser.find_element(By.ID, 'target')
#     ActionChains(browser).drag_and_drop(obj, target).pause(3).perform()  # используют метод не по условию
#     print(browser.find_element(By.ID, 'password').text)



# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/7/7.3.1/index.html')
#
#     human = driver.find_element(By.ID, 'draggable')
#
#     actions = ActionChains(driver)
#     actions.drag_and_drop_by_offset(human, 0, -200).perform()
#
#     print(
#         WebDriverWait(driver, 3).until(
#             EC.visibility_of_element_located((By.ID, 'password'))
#         ).text
#     )



# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/7/7.3.1/index.html')
#
#     piter_griffin = browser.find_element(By.CSS_SELECTOR, '#draggable')
#     swimming_pool = browser.find_element(By.CSS_SELECTOR, '#target')
#
#     actions = ActionChains(browser)
#     actions.drag_and_drop(piter_griffin, swimming_pool).perform()
#
#     password = browser.find_element(By.CSS_SELECTOR, '#password').text
#     print(password)