import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

start_time = time.time()

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.2/index.html")

    list_input = []
    processed_count = 0

    while processed_count < 100:
        input_tags = browser.find_elements(By.CLASS_NAME, 'interactive')
        for tag_input in input_tags:
            if tag_input not in list_input:
                tag_input.send_keys('TEXT')
                tag_input.send_keys(Keys.ENTER)
                tag_input.send_keys(Keys.ARROW_DOWN)
                list_input.append(tag_input)
                processed_count += 1
                # print(f"Обработано полей: {processed_count}")   # отладка
                break
        time.sleep(0.1)

    end_time = time.time()
    print('Время работы кода: ', end_time - start_time)  # Время работы кода:  23.651110887527466
    print(browser.find_element(By.ID, 'hidden-password').text)

# Время работы кода: 13.550416946411133 (без единого time.sleep())


# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.2/index.html')
#     i = 0
#     while i != 100:
#         fields  = browser.find_elements(By.CLASS_NAME, 'interactive')
#         for field in fields[i:]:
#             field.send_keys('hello', Keys.ENTER, Keys.ARROW_DOWN)
#         i = len(fields)
#
#     print(browser.find_element(By.ID, 'hidden-password').text)


# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# url = "https://parsinger.ru/selenium/7/7.2/index.html"
# start_time = time.time()
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     for i in range(1, 101):
#         input_field = browser.find_element(By.XPATH, f"//div[{i}]/input")
#         input_field.send_keys("a")
#         input_field.send_keys(Keys.ENTER)
#         input_field.send_keys(Keys.ARROW_DOWN)
#
#     result = browser.find_element(By.ID, "hidden-password").text
#     end_time = time.time()
#     print('Время работы кода: ', end_time - start_time) # Время работы кода:  12.761056900024414
#     print(result)




# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
#     list_input = []
#     while True:
#         input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
#         for tag_input in input_tags:
#             if tag_input not in list_input:
#                 tag_input.send_keys(Keys.DOWN)
#                 tag_input.send_keys('Текст')
#                 tag_input.send_keys(Keys.ENTER)
#                 list_input.append(tag_input)
#
#                 if len(list_input) >= 100:
#                     pswd = browser.find_element(By.ID,'hidden-password').text
#                     print(pswd)
#                     browser.quit()



# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
#     current_input = browser.find_element(By.TAG_NAME, "input")
#
#     for _ in range(100):
#         current_input.send_keys("...", Keys.ENTER, Keys.ARROW_DOWN)
#         current_input = browser.switch_to.active_element
#     print(browser.find_element(By.ID, "hidden-password").text)



# while True:
#     fields = browser.find_elements(By.XPATH, '//div[@data-filled="false"]/../input')
#     if not fields: break
#     fields[0].send_keys("lol", Keys.ENTER, Keys.DOWN)
# print(browser.find_element(By.ID, "hidden-password").text)



# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
#     field = browser.find_element(By.TAG_NAME, 'input').send_keys('text')
#     action = webdriver.ActionChains(browser)
#
#     for _ in range(100):
#         action.send_keys(Keys.ENTER).send_keys(Keys.ARROW_DOWN).send_keys('text').perform()
#         time.sleep(0.1)
#     time.sleep(20)



# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.2/index.html')
#     actions = ActionChains(browser)
#     for i in range(1, 101):
#         actions.send_keys_to_element(browser.find_element(By.CSS_SELECTOR, f'.input-container .input-wrapper:nth-child({i}) .interactive'), i).send_keys(Keys.ENTER).send_keys(Keys.ARROW_DOWN).perform()
#     print(browser.find_element(By.ID, 'hidden-password').text)



# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
#     list_input = []
#     processed_count = 0
#     while processed_count < 100:
#         input_tags = browser.find_elements(By.CLASS_NAME, 'interactive')
#         for i in range(len(input_tags)):
#             if processed_count >= 100:
#                 break
#
#             tag_input = input_tags[i]
#             if tag_input not in list_input:
#                 tag_input.send_keys('TEXT')
#                 tag_input.send_keys(Keys.ENTER)
#                 tag_input.send_keys(Keys.ARROW_DOWN)
#                 time.sleep(0.1)
#                 list_input.append(tag_input)
#                 processed_count += 1
#                 print(f"Обработано полей: {processed_count}")
#                 input_tags = browser.find_elements(By.CLASS_NAME, 'interactive')
#         time.sleep(0.5)
#     password = browser.find_element(By.ID, 'hidden-password')
#     print(password.text)


