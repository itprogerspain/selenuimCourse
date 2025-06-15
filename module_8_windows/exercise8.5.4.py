import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    browser.set_window_size(571, 702)
    print(browser.find_element(By.ID, 'result').text)



# 1684163857416385746374

'''Небольшой алгоритм, чего нужно делать. Спасибо автору, самые сложные цифры - это размеры 
внутренней видимой области страницы он нам дал. Просто заходим на наш сайт абы как и смотрим 
что у нас там с этими цифрами. Сохраняем их себе наподобие высота_внутренняя, так же и с шириной. 
Через метод get_window_size, получаем размеры, но уже внешние. От внешних отняв внутренние, 
получим что наш браузер тратит на интерфейс (16 и 147). А теперь самое интересное - говорим методом 
set_window_size установить размеры высоты 555 плюс интерфейс, так же и ширины. В спане будет наше 
число.
'''


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# URL = "https://parsinger.ru/window_size/1/"
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
#     driver.set_window_size(555 + target_width, 555 + target_height)
#     time.sleep(5)
#     result = driver.find_element(By.ID, 'result').text
#     print(result)



# import time
# from selenium.webdriver.common.by import By
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/window_size/1/')
#
#     window_size = browser.get_window_size()
#     width_border = window_size['width'] - browser.execute_script(
#         'return window.innerWidth'
#     )
#     height_border = window_size['height'] - browser.execute_script(
#         'return window.innerHeight'
#     )
#
#     browser.set_window_size(555 + width_border, 555 + height_border)
#     time.sleep(0.5)
#
#     result = browser.find_element(By.CSS_SELECTOR, '#result')
#     print(result.text)




# link = "http://parsinger.ru/window_size/1/"
# options = Options()
# options.add_argument("--window-size=555,555")
# browser = webdriver.Chrome(options=options)
# browser.get(link)
# delta_y = browser.execute_script("return window.innerHeight")
# delta_x = browser.execute_script("return window.innerWidth")
# browser.set_window_size((555 + (555 - int(delta_x))), (555 + (555 - int(delta_y))))
# result = browser.find_element(By.CSS_SELECTOR, "#result")
# print(result.text)




# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
#
# with Chrome() as browser:
#     browser.get('http://parsinger.ru/window_size/1/')
#
#     browser.set_window_size(555, 555)
#     dif_w = 555 - int(browser.find_element(By.ID, 'width').text.split()[-1])
#     dif_h = 555 - int(browser.find_element(By.ID, 'height').text.split()[-1])
#     browser.set_window_size(555 + dif_w, 555 + dif_h)
#     print(browser.find_element(By.ID, 'result').text)