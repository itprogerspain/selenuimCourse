from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')

    wait = WebDriverWait(browser, 25)
    loc_usd_rate = (By.ID, 'usd-rate')
    loc_secret_code = (By.ID, 'secret-code')
    exp_text = '75.50 ₽'

    try:
        wait.until(EC.text_to_be_present_in_element(loc_usd_rate, exp_text))
    except TimeoutException:
        print('TimeoutException_1')

    try:
        print(wait.until(EC.visibility_of_element_located(loc_secret_code)).text)
    except TimeoutException:
        print('TimeoutException_2')




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# with webdriver.Chrome() as browser:
#     # Открытие страницы тренажера
#     browser.get("https://parsinger.ru/selenium/9/9.6.1/index.html")
#
#     # Находим элемент с курсом доллара
#     usd_rate_element = (By.ID, "usd-rate")
#
#     # Ожидаем, когда курс доллара достигнет целевого значения "75.50 ₽"
#     WebDriverWait(browser, 60).until(
#         EC.text_to_be_present_in_element(usd_rate_element, "75.50 ₽")
#     )
#
#     print("Курс доллара достиг целевого значения!")
#
#     # Находим и извлекаем секретный код
#     secret_code = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "secret-code")))
#
#     print(f"Секретный код: {secret_code.text}")
#
#     # Даем время, чтобы увидеть результат
#     time.sleep(5)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.6.1/index.html")
#     WebDriverWait(browser, 60).until(
#         EC.text_to_be_present_in_element((By.ID, "usd-rate"), "75.50 ₽")
#     )
#     print(
#         WebDriverWait(browser, 5)
#         .until(EC.visibility_of_element_located((By.ID, "code-container")))
#         .text.split("; ")[1]
#     )




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.6.1/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     course_usd = ("id", "usd-rate")
#     waiter = WebDriverWait(driver, 50)
#     try:
#         waiter.until(ec.text_to_be_present_in_element(course_usd, "75.50 ₽"))
#         result = driver.find_element("id", "secret-code").text
#         print("Result is:", result)
#     except:
#         print("Не дождался получается!")




# from selenium.common.exceptions import TimeoutException
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.6.1/index.html")
#     locator = (By.ID, 'usd-rate')
#     expected_text = "75.50 ₽"
#     while True:
#         try:
#             WebDriverWait(browser, 1). until(EC.text_to_be_present_in_element (locator, expected_text))
#             break
#         except TimeoutException:
#             continue
#
#     WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.ID,'secret-code')))
#     print(browser.find_element(By.ID,'secret-code').text)