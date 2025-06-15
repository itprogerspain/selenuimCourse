from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    pins = browser.find_elements(By.CLASS_NAME, 'pin')

    for pin in pins:
        pin_code = pin.text
        browser.find_element(By.ID, 'check').click()
        time.sleep(0.1)
        alert = browser.switch_to.alert
        alert.send_keys(pin_code)
        alert.accept()
        time.sleep(0.1)
        result = browser.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            print(result)
            break



# 1261851212132345456274632




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
#     pin_code = [x.text for x in browser.find_elements(By.CLASS_NAME, 'pin')]
#     for pin in pin_code:
#         browser.find_element(By.ID, 'check').click()
#         confirm = browser.switch_to.alert
#         time.sleep(.3)
#         confirm.send_keys(pin)
#         confirm.accept()
#         result = browser.find_element(By.ID, 'result').text
#         if result.isdigit():
#             print(result)




# from selenium import webdriver
#
# URL = "https://parsinger.ru/selenium/5.8/3/index.html"
# with webdriver.Edge() as driver:
#     driver.get(url=URL)
#     pins = [item.text for item in driver.find_elements("class name", "pin")]
#     for pin in pins:
#         driver.find_element("id", "check").click()
#         prompt = driver.switch_to.alert
#         prompt.send_keys(pin)
#         prompt.accept()
#         result = driver.find_element("id", "result").text
#         if result != "Неверный пин-код":
#             print("Result is:", result)
#             break




# import time
# from tqdm import tqdm
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# start_time = time.perf_counter()
# url = r'https://parsinger.ru/selenium/5.8/3/index.html'
#
# # открытие селениум в интерактивном режиме
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(1)
#
#     pins = browser.find_elements(By.CSS_SELECTOR, 'span.pin')
#     check = browser.find_element(By.ID, 'check')
#     password = browser.find_element(By.ID, 'result')
#     for pin in pins:
#         extracted_text = pin.text
#         check.click()
#         prompt = browser.switch_to.alert
#         prompt.send_keys(extracted_text)
#         prompt.accept()
#         if password.text != 'Неверный пин-код':
#             print(password.text)
#             break
#
# end_time = time.perf_counter()
# print(f"Время выполнения программы: {end_time - start_time} cек.")




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# if __name__ == '__main__':
#     try:
#         with webdriver.Chrome() as browser:
#             browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
#             pincode = browser.find_elements(By.CLASS_NAME, 'pin')
#             check_button = browser.find_element(By.ID, 'check')
#
#             for pin in pincode:
#                 extract = pin.text
#                 check_button.click()
#                 enter_field = browser.switch_to.alert
#                 enter_field.send_keys(extract)
#                 enter_field.accept()
#
#                 result = browser.find_element(By.ID, 'result').text
#                 if result != 'Неверный пин-код':
#                     print(result)
#
#     except Exception as e:
#         print(f"Ошибка: {e}")