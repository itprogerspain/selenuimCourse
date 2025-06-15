import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

count = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    div = browser.find_element(By.CSS_SELECTOR, '#scroll-container > div')

    for _ in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 600).perform()
        time.sleep(0.5)
    numbers = browser.find_elements(By.TAG_NAME, 'span')
    for number in numbers:
        if number.text:
            count += int(number.text)
    print(count)


# from selenium.webdriver import Chrome, Keys, ActionChains
#
#
# URL = "http://parsinger.ru/infiniti_scroll_1/"
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     for i in range(100):
#         action.send_keys(Keys.TAB).pause(0.05).perform()
#     containers = [int(num.text) for num in driver.find_elements("css selector", "#scroll-container span")]
#     print("Result is:", sum(containers))



# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/infiniti_scroll_1/")
#     actions = ActionChains(browser)
#     res = 0
#     while True:
#         actions.send_keys(Keys.TAB).send_keys(Keys.SPACE).perform()
#         span = browser.switch_to.active_element.find_element(By.XPATH, "..")
#         if span.text.isdigit():
#             res += int(span.text)
#         if span.get_attribute("class") == "last-of-list":
#             break


# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://parsinger.ru/infiniti_scroll_1/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(0.5)
#     count = 0
#     checking = []
#     result = []
#     while True:
#         input_list = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
#
#         for inp in input_list:
#             if inp not in checking:
#                 inp.send_keys(Keys.DOWN)
#                 count += 1
#                 checking.append(inp)
#
#         span_list = [result.append(int(x.text)) for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span') if int(x.text) not in result]
#         break_loop = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
#         if break_loop:
#             break
#     print(f'Результат: {sum(result)}')



# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#
#     div = browser.find_element(By.CSS_SELECTOR, '#scroll_container > div')
#
#     while True:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
#         time.sleep(0.5)
#
#         # Проверяем, стал ли элемент с классом 'last-of-list' видимым
#         try:
#             last_element = WebDriverWait(browser, timeout=1).until(
#                 EC.visibility_of_element_located((By.CLASS_NAME, 'last-of-list'))
#             )
#             # Если элемент видим, прерываем цикл
#             break
#         except:
#             # Если элемент невидим или не найден, продолжаем скроллить
#             pass
#
#     # Суммируем числа из всех span после завершения скроллинга
#     count = 0
#     spans = browser.find_elements(By.TAG_NAME, 'span')
#     for span in spans:
#         if span.text:
#             count += int(span.text)
#
#     print(count)
#



# with webdriver.Chrome(options=options_chrome) as browser:
#     try:
#         done_list = []
#         result = []
#         browser.get(url)
#
#         while len(result) < 100:
#             actions = ActionChains(browser)
#             check_boxes = [check for check in browser.find_elements(By.CSS_SELECTOR,'span[id]') if check.text]
#
#             for item in check_boxes:
#                 if item not in done_list:
#                     done_list.append(item)
#                     result.append(int(item.text))
#                     item.find_element(By.CSS_SELECTOR,'input').send_keys(Keys.TAB)
#
#         print(sum(result))




# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#
#     scrolling_container = browser.find_element(
#         By.CSS_SELECTOR, '#scroll-container'
#     )
#
#     data = []
#     numbers = []
#
#     while True:
#         number_elements = scrolling_container.find_elements(
#             By.CSS_SELECTOR, 'span'
#         )
#         for element in number_elements:
#             if element not in data:
#                 element.find_element(By.CSS_SELECTOR, 'input').send_keys(
#                     Keys.DOWN
#                 )
#                 data.append(element)
#                 numbers.append(int(element.text))
#             if element.get_attribute('class') == 'last-of-list':
#                 break
#         else:
#             continue
#         break
#
#     print(sum(numbers))











