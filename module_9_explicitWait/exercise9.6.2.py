from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')

    wait = WebDriverWait(browser, 20)
    loc_recipe_field = (By.ID, 'recipe_field')
    loc_password = (By.ID, 'password')
    exp_text = 'Селениумий'

    browser.find_element(By.ID, 'ask-jaskier').click()

    try:
        wait.until(EC.text_to_be_present_in_element_value(loc_recipe_field, exp_text))
    except TimeoutException:
        print('TimeoutException_1')

    try:
        print(wait.until(EC.visibility_of_element_located(loc_password)).text)
    except TimeoutException:
        print('TimeoutException_2')

# КаэрМорхен1258



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# with webdriver.Chrome() as browser:
#     # Открытие страницы тренажера
#     browser.get("http://127.0.0.1:5500/9.Waits/9.6.Waiting%20text/9.6.2.text_to_be_present_in_element_value/index.html")
#
#     # Нажатие на кнопку
#     ask_button = browser.find_element(By.ID, "ask-jaskier")
#     ask_button.click()
#
#     # Ожидание появления текста "Селениумий" в поле ввода
#     recipe_field = (By.ID, "recipe_field")
#     WebDriverWait(browser, 20).until(
#         EC.text_to_be_present_in_element_value(recipe_field, "Селениумий")
#     )
#
#     # Проверяем, что пароль отображается
#     WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "password-container"))
#     )
#
#     # Получение пароля
#     password_element = browser.find_element(By.ID, "password")
#     password = password_element.text
#
#     print(f"Пароль для подтверждения задания: {password}")
#     time.sleep(3)




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
#     browser.get("https://parsinger.ru/selenium/9/9.6.2/index.html")
#     browser.find_element(By.ID, "ask-jaskier").click()
#     WebDriverWait(browser, 30).until(
#         EC.text_to_be_present_in_element_value((By.ID, "recipe_field"), "Селениумий")
#     )
#     print(
#         WebDriverWait(browser, 10)
#         .until(EC.visibility_of_element_located((By.ID, "password")))
#         .text
#     )



# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.6.2/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     driver.find_element("id", "ask-jaskier").click()
#     recipe = ("id", "recipe_field")
#     password = ("id", "password")
#     try:
#         WebDriverWait(driver, 20).until(ec.text_to_be_present_in_element_value(recipe, "Селениумий"))
#         result = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(password)).text
#         print("Result is:", result)
#     except:
#         print("Время и стекло")