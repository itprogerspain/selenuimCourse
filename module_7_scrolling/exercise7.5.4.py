from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.common.by import By


count = 0

with Chrome() as browser:
    browser.get("https://parsinger.ru/infiniti_scroll_3/")
    action = ActionChains(browser)
    for _ in range(6):
        action.send_keys(Keys.TAB).pause(0.5).perform()
        for _ in range(10):
            action.send_keys(Keys.END).pause(0.3).perform()
            numbers = browser.find_elements(By.TAG_NAME, 'span')
    for number in numbers:
        if number.text.isdigit():
            count += int(number.text)

    print(count)




# from selenium.webdriver import Chrome, Keys, ActionChains
# from time import perf_counter
#
#
# URL = "https://parsinger.ru/infiniti_scroll_3/"
# result = []
#
# def get_sum(box):
#     action.move_to_element(box).click().perform()
#     while True:
#         action.send_keys(Keys.END).pause(0.05).perform()
#         spans = box.find_elements("xpath", ".//span[contains(@id, '_index_')]")
#         if len(spans) == 100:
#             break
#     return sum([int(span.text) for span in spans])
#
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     containers = driver.find_elements("xpath", "//div[contains(@id, 'scroll-container')]")
#     for i in range(5):
#         result.append(get_sum(containers[i]))
#     print("Result is:", sum(result))
# Верное решение #1481795701




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_3/')
#     for _ in range(10):
#         for container_num in range(1, 6):
#             ActionChains(browser).move_to_element(
#                 browser.find_element(By.XPATH, f'//*[@id="scroll-container_{container_num}"]/div'))\
#                 .scroll_by_amount(0, 450)\
#                 .perform()
#     res = 0
#     for elem in browser.find_elements(By.TAG_NAME, 'span'):
#         if elem.text.isdigit():
#             res += int(elem.text)
#     time.sleep(5)
#     print(res)




# От Хошева с использованием расширения координаты


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# start = time.time()
# url = 'http://parsinger.ru/infiniti_scroll_3/'
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
# result = []
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     browser.get(url)
#     browser.set_window_size(1024, 720)
#
#     while True:
#         ActionChains(browser).scroll(85, 275, 85, 275).perform()
#         ActionChains(browser).scroll(280, 300, 280, 300).perform()
#         ActionChains(browser).scroll(480, 300, 480, 300).perform()
#         ActionChains(browser).scroll(680, 320, 680, 320).perform()
#         ActionChains(browser).scroll(900, 300, 900, 300).perform()
#
#         catch_last_elem = [x for x in browser.find_element(By.ID, 'scroll-container_5').find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
#         if catch_last_elem:
#             [result.append(int(x.text)) for x in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')]
#             break
#
# print(sum(result))
# print(f'Time is running{time.time() - start}')


