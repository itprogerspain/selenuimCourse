from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product
import time


window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    combinations = list(product(window_size_x, window_size_y))
    for x, y in product(window_size_x, window_size_y):
        browser.set_window_size(x + 16, y + 147)
        # for i in combinations:
    #     browser.set_window_size(i[0] + 16, i[1] + 147)
        time.sleep(0.5)
        result = browser.find_element(By.ID, 'result').text
        if result:
            print(result)
            break



# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# url = 'http://parsinger.ru/window_size/2/index.html'
# size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     for x in size_x:
#         for y in size_y:
#             browser.set_window_size(16 + x, 133 + y)
#             try:
#                 res = browser.find_element(By.ID, 'result').text
#                 if res:
#                     print(res)
#             except:
#                 pass


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import re
#
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# with webdriver.Chrome() as browser:
#    for x in window_size_x:
#         for y in window_size_y:
#             browser.set_window_size(x + 16, y + 147)
#             browser.get('http://parsinger.ru/window_size/2/index.html')
#             if len(browser.find_element(By.ID,'result').text) > 1:
#                 print(browser.find_element(By.ID, 'result').text)
#                 break



# with webdriver.Chrome(options=options_chrome) as browser:
#     try:
#         browser.get(url)
#         actions = ActionChains(browser)
#         for size in range(len(window_size_x)):
#             for i in range(len(window_size_y)):
#                 if browser.find_element(By.ID,'result').text: break
#                 browser.set_window_size(window_size_x[size]+16,window_size_y[i]+147)
#         time.sleep(10)





# from selenium.webdriver.common.by import By
# from selenium_scripts.browser_setup import browser
#
# # fmt: off
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# # fmt: on
#
# with browser:
#     browser.get('https://parsinger.ru/window_size/2/index.html')
#
#     window_size = browser.get_window_size()
#     width_border = window_size['width'] - browser.execute_script(
#         'return window.innerWidth'
#     )
#     height_border = window_size['height'] - browser.execute_script(
#         'return window.innerHeight'
#     )
#
#     for x in window_size_x:
#         for y in window_size_y:
#             browser.set_window_size(x + width_border, y + height_border)
#             result = browser.find_element(By.CSS_SELECTOR, '#result').text
#             if result:
#                 right_size = {'width': x, 'height': y}
#                 print(right_size, result)
#                 break




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = "https://parsinger.ru/window_size/2/index.html"
#
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# # Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument("--headless=new")
#
#
# def get_result(url: str):
#     with webdriver.Chrome(options_chrome) as driver:
#         driver.get(url)
#
#         def_width = driver.get_window_size()["width"]
#         def_height = driver.get_window_size()["height"]
#
#         work_width = driver.execute_script("return window.innerWidth;")
#         work_height = driver.execute_script("return window.innerHeight;")
#
#         diff_width = def_width - work_width
#         diff_height = def_height - work_height
#
#         for x in window_size_x:
#             for y in window_size_y:
#                 driver.set_window_size(x + diff_width, y + diff_height)
#                 result = driver.find_element(By.ID, "result").text
#
#                 if result:
#                     print(result)
#
#
# get_result(URL)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# URL = "https://parsinger.ru/window_size/2/index.html"
#
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# with webdriver.Chrome() as driver:
#     driver.get(URL)
#     inner_width = int(driver.find_element(By.ID, 'width').text.split(": ")[1])
#     inner_height = int(driver.find_element(By.ID, 'height').text.split(": ")[1])
#     outer_width = driver.get_window_size().get('width')
#     outer_height = driver.get_window_size().get('height')
#
#     target_width = outer_width - inner_width
#     target_height = outer_height - inner_height
#
#     for x in window_size_x:
#         for y in window_size_y:
#             driver.set_window_size(x + target_width, y + target_height)
#
#             try:
#                 # Ожидание обновления текста в элементе result
#                 result = WebDriverWait(driver, 1).until(
#                     EC.text_to_be_present_in_element((By.ID, 'result'), '')
#                 )
#                 result_text = driver.find_element(By.ID, 'result').text
#                 if result_text:
#                     print(f"{x} x {y}")
#                     print(result_text)
#                     break
#             except:
#                 # Если не обновилось в течение 1 секунды, продолжить
#                 continue
