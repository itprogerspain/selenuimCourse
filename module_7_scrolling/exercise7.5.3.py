# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# count = 0
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.CSS_SELECTOR, '#scroll-container > div')
#
#     for _ in range(10):
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 600).perform()
#         time.sleep(0.5)
#     numbers = browser.find_elements(By.TAG_NAME, 'p')
#     for number in numbers:
#         if number.text:
#             count += int(number.text)
#     print(count)






from selenium.webdriver import Chrome, Keys, ActionChains

URL = "http://parsinger.ru/infiniti_scroll_2/"
with Chrome() as driver:
    driver.get(url=URL)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB).perform()
    for _ in range(20):
        action.send_keys(Keys.END).pause(0.5).perform()
    nums = [int(num.text) for num in driver.find_elements("css selector", "#scroll-container p")]
print("Result is:", sum(nums))




# Cразу выкладывает решение на степик

# from time import sleep
#
# from environs import Env
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait
#
# url = 'https://parsinger.ru/infiniti_scroll_2/'
# stepic = 'https://stepik.org/lesson/732069/step/3?unit=733602'
#
# env = Env()
# env.read_env(recurse=False)
#
# options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
#
# with webdriver.Chrome(options=options) as driver:
#     wait = WebDriverWait(driver, 15)
#     driver.get(url)
#     action = ActionChains(driver)
#
#     while True:
#         action \
#             .move_to_element(driver.find_element
#                              ('xpath', '//div[@id="scroll-container"]/div')) \
#             .scroll_by_amount(0, 1000) \
#             .pause(1) \
#             .perform()
#         try:
#             driver.find_element('class name', 'last-of-list')
#             break
#         except NoSuchElementException:
#             pass
#
#     lst = driver.find_element('id', 'scroll-container').text
#     result = sum(int(item) for item in lst.split())
#
#     driver.switch_to.new_window()
#     driver.get(stepic)
#     driver.add_cookie({'name': 'sessionid', 'value': env('STEPIK_SESSIONID')})
#     driver.refresh()
#     wait.until(
#         ec.visibility_of_element_located(('xpath', '//div[@class="attempt"]//input'))
#     ).send_keys(result)
#     wait.until(
#         ec.element_to_be_clickable(('xpath', '//button[@class="submit-submission"]'))
#     ).click()
#     sleep(5)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = 'https://parsinger.ru/infiniti_scroll_2/'
#
# with webdriver.Chrome() as browser:
#     browser.get(URL)
#
#     # атрибут top этого элемента будет меняться при прокрутке
#     scroll_container = browser.find_element(By.XPATH, '//div[@id="scroll-container"]/div')
#     scroll_origin = ScrollOrigin.from_element(scroll_container)
#
#     for _ in range(6):
#         ActionChains(browser) \
#             .scroll_from_origin(scroll_origin, 0, 1000) \
#             .perform()
#
#         # ждём, пока пропадёт спиннер подгрузки (вместо time.sleep)
#         WebDriverWait(browser, 5).until(
#             EC.invisibility_of_element_located((By.CLASS_NAME, 'spinner')))
#
#     numbers = browser.find_elements(By.XPATH, '//div[@id="scroll-container"]/p')
#     res = sum(int(num.text) for num in numbers)
#     print(res)





# От Хошева При помощи расширения coordinates

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     url = 'http://parsinger.ru/infiniti_scroll_2/'
#     browser.get(url)
#     browser.set_window_size(1920, 1080)
#     while True:
#         ActionChains(browser).scroll(800, 400, 800, 400).perform()
#         time.sleep(0.2)
#         attrbt = [x.get_attribute('id') for x in browser.find_elements(By.TAG_NAME, 'p') if x.get_attribute('class')]
#         if attrbt:
#             break
#     res = [int(x.text) for x in browser.find_elements(By.TAG_NAME, 'p') if x.text]
#     print(sum(res))




# import time
# from selenium.webdriver import Keys, ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# res = 0
# list_span = []
# with webdriver.Chrome() as browser:
#     browser.get("http://parsinger.ru/infiniti_scroll_2/")
#     div = browser.find_element(By.ID, 'scroll-container')
#     action = ActionChains(browser)
#
#     while len(list_span) < 100:
#         action.click(div).send_keys(Keys.DOWN).perform()
#         time.sleep(0.1)  # небольшая задержка для подгрузки элементов
#
#         spans = div.find_elements(By.TAG_NAME, 'p')
#         for span in spans:
#             if span.text.isdigit() and span.text not in list_span:
#                 list_span.append(span.text)
#
#                 if len(list_span) == 100:
#                     break
#
# for i in list_span:
#     res += int(i)
# print(res)

