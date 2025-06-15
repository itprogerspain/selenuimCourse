from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/8/8.1.2/index.html")
    x = browser.window_handles
    urls = [a.get_attribute('href') for a in browser.find_elements(By.TAG_NAME, 'a')]

    count = 0
    for url in urls:
        browser.switch_to.new_window("tab")
        browser.get(url)
        time.sleep(4)
        numbers = browser.find_elements(By.CLASS_NAME, 'number')
        for number in numbers:
            count += int(number.text)
    browser.switch_to.window(x[0])
    browser.find_element(By.ID, 'sumInput').send_keys(count)
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'passwordDisplay').text)
    time.sleep(3)





# import time
# from selenium.webdriver import Chrome
#
# URL = "https://parsinger.ru/selenium/8/8.1.2/"
# result = []
# with Chrome() as driver:
#     driver.get(url=URL + "index.html")
#     links = [item.get_attribute("href") for item in driver.find_elements("css selector", ".code-links a")]
#     for link in links:
#         driver.switch_to.new_window("tab")
#         driver.get(url=link)
#         time.sleep(3)
#         nums = [int(num.text) for num in driver.find_elements("class name", "number")]
#         result.append(sum(nums))
#     driver.switch_to.window(driver.window_handles[0])
#     driver.find_element("id", "sumInput").send_keys(sum(result))
#     driver.find_element("id", "checkButton").click()
#     password = driver.find_element("id", "passwordDisplay").text
#     print(password)






# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/selenium/8/8.1.2/index.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     input_field = browser.find_element(By.ID, "sumInput")
#     button = browser.find_element(By.ID, "checkButton")
#     links = browser.find_elements(By.TAG_NAME, "a")
#     home_page = browser.current_window_handle
#
#     total = 0
#     for link in links:
#         url = link.get_attribute("href")
#         browser.switch_to.new_window('tab')
#         browser.get(url=url)
#         time.sleep(5)
#
#         numbers = browser.find_elements(By.CLASS_NAME, "number")
#         total += sum(int(number.text) for number in numbers)
#
#         browser.switch_to.window(home_page)
#
#     input_field.send_keys(total)
#     button.click()
#
#     password = browser.find_element(By.ID, "passwordDisplay").text
#     print(password)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# url_base = r'https://parsinger.ru/selenium/8/8.1.2/index.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url_base)
#     descriptor = browser.current_window_handle
#     time.sleep(1)
#     all_urls = []
#     urls = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
#     for url in urls:
#         page = url.get_attribute('href')
#         # print('page =', page)
#         all_urls.append(page)
#     # print('all_urls =', all_urls)
#     total = 0
#     for url in all_urls:
#         browser.switch_to.new_window("tab")
#         browser.get(url)
#         time.sleep(5)
#         num = sum(map(int, browser.find_element(By.CSS_SELECTOR, 'div.numbers-container').text.split('\n')))
#         # print(num)
#         total += num
#
#     browser.switch_to.window(descriptor)
#     input = browser.find_element(By.CSS_SELECTOR, 'input[type="number"]').send_keys(total)
#     button = browser.find_element(By.ID, 'checkButton').click()
#     time.sleep(1)
#     password = browser.find_element(By.ID, 'passwordDisplay').text
#     print(password)
#
# '''
# TH3-G4T3S-0F-H3LL-4R3-0P3N
# '''
#





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://parsinger.ru/selenium/8/8.1.2/index.html'
# result = []
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     main_window = browser.current_window_handle
#     links = [link.get_attribute('href') for link in browser.find_elements(By.CSS_SELECTOR, 'div.code-links > a')]
#     for i in range(len(links)):
#         browser.switch_to.new_window('tab')
#         browser.get(links[i])
#         time.sleep(4)
#         result.append(sum([int(num.text) for num in browser.find_elements(By.CSS_SELECTOR, 'div.number')]))
#     browser.switch_to.window(main_window)
#     browser.find_element(By.ID, 'sumInput').send_keys(sum(result))
#     browser.find_element(By.ID, 'checkButton').click()
#     print(browser.find_element(By.ID, 'passwordDisplay').text)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# total = 0
# with webdriver.Chrome() as browser:
#     browser.get(f'https://parsinger.ru/selenium/8/8.1.2/index.html')
#     links = browser.find_elements(By.TAG_NAME, 'a')
#     urls = [link.get_attribute('href') for link in links]
#     for url in urls:
#         browser.switch_to.new_window('tab')
#         browser.get(url)
#         time.sleep(3)
#         total += sum([int(number.text) for number in browser.find_elements(By.CLASS_NAME, 'number')])
#     browser.switch_to.window(browser.window_handles[0])
#     browser.find_element(By.ID, 'sumInput').send_keys(total)
#     browser.find_element(By.ID, 'checkButton').click()
#     print(browser.find_element(By.ID, 'passwordDisplay').text)





# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     base_url = "https://parsinger.ru/selenium/8/8.1.2/"
#     index_url = f"{base_url}index.html"
#
#     browser.get(index_url)
#     # Сохраняем дескриптор (handle) главной страницы, чтобы потом можно было к ней вернуться
#     main_handle = browser.current_window_handle
#     print("Главная страница открыта, таймер запущен.")
#
#     # Собираем список ссылок на 5 страниц
#     pagination = browser.find_elements(By.CSS_SELECTOR, "a")
#     all_page_links = [link.get_attribute("href") for link in pagination]
#
#     # Итерируем по ссылками и открываем каждую в новом окне:
#     for page in all_page_links:
#         browser.switch_to.new_window("tab")
#         browser.get(page)
#     # Ждем 3 секунды, чтобы на страницах успели появиться числа
#     time.sleep(3)
#     # Список для хранения всех чисел
#     all_nums = []
#     # Перебираем все вкладки, кроме главной
#     for handle in browser.window_handles[1:]:
#         browser.switch_to.window(handle)
#         numbers = browser.find_elements(By.CLASS_NAME, "number")
#         for number in numbers:
#             all_nums.append(int(number.text))
#         browser.close()
#     # Переключаемся обратно на главную страницу
#     browser.switch_to.window(main_handle)
#     field = browser.find_element(By.ID, "sumInput")
#     field.send_keys(str(sum(all_nums)))
#     time.sleep(3)
#     check_btn = browser.find_element(By.ID, "checkButton")
#     check_btn.click()
#     print(browser.find_element(By.ID, "passwordDisplay").text)