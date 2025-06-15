from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product
import time


window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    combinations = list(product(window_size_x, window_size_y))
    for x, y in product(window_size_x, window_size_y):
        browser.set_window_size(x + 16, y + 147)
        time.sleep(0.1)
        result = browser.find_element(By.ID, 'result').text
        if result:
            actual_size = browser.get_window_size()
            actual_size['width'] -= 16
            actual_size['height'] -= 147
            print(actual_size)
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
#             if browser.find_element(By.ID, 'result').text.isdigit():
#                 print('{'  f"'width': {x}, 'height': {y}"  '}')



# from itertools import product
# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/window_size/2/index.html"
# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# with Chrome() as driver:
#     driver.get(url=URL)
#     for size in list(product(window_size_x, window_size_y)):
#         driver.set_window_size(size[0] + 16, size[-1] + 147)
#         result = driver.find_element("id", "result").text
#         window_size = driver.get_window_size()
#         window_size["width"] -= 16
#         window_size["height"] -= 147
#         if result:
#             print("Result is:", window_size)
#             break



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



# import itertools
# link = "http://parsinger.ru/window_size/2/index.html"
# browser = webdriver.Chrome()
# browser.get(link)
# result = browser.find_element(By.CSS_SELECTOR, "#result")
# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# for x, y in itertools.product(window_size_x, window_size_y):
#     browser.set_window_size(x + 16, y + 147)
#     time.sleep(.001)
#     if result.text:
#         print(result.text)
#         print(browser.get_window_size())
#         print(browser.execute_script("return window.innerHeight"))
#         print(browser.execute_script("return window.innerWidth"))
#         break
# browser.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://parsinger.ru/window_size/2/index.html"

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as driver:
    driver.get(URL)
    inner_width = int(driver.find_element(By.ID, 'width').text.split(": ")[1])
    inner_height = int(driver.find_element(By.ID, 'height').text.split(": ")[1])
    outer_width = driver.get_window_size().get('width')
    outer_height = driver.get_window_size().get('height')

    target_width = outer_width - inner_width
    target_height = outer_height - inner_height

    for x in window_size_x:
        for y in window_size_y:
            driver.set_window_size(x + target_width, y + target_height)

            try:
                # Ожидание обновления текста в элементе result
                result = WebDriverWait(driver, 1).until(
                    EC.text_to_be_present_in_element((By.ID, 'result'), '')
                )
                result_text = driver.find_element(By.ID, 'result').text
                if result_text:
                    res_dct = {'width': x, 'height': y}
                    print(res_dct)
                    print(result_text)
                    break
            except:
                # Если не обновилось в течение 1 секунды, продолжить
                continue