from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')

    wait = WebDriverWait(browser, 15)

    browser.find_element(By.ID, 'address').send_keys('fkjbnxkfjbn')
    browser.find_element(By.ID, 'payment').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Карта']"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'submit-order'))).click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'spinner')))
    wait.until(EC.element_to_be_clickable((By.ID, 'confirm-address'))).click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'modal')))
    wait.until(EC.element_to_be_clickable((By.ID, 'get-code'))).click()
    print(wait.until(EC.visibility_of_element_located((By.ID, 'result'))).text)


# 5TR4NG3R-D3M0G0N-001


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# url = "https://parsinger.ru/selenium/9/9.7.1/index.html"
#
# with webdriver.Chrome() as browser:
#     try:
#         # Открытие страницы тренажера
#         print("Открываем страницу тренажера...")
#         browser.get(url)
#
#         # Создание объекта ожидания
#         wait = WebDriverWait(browser, 10)
#
#         # Ожидание загрузки страницы
#         wait.until(EC.presence_of_element_located((By.ID, "address")))
#
#         # Заполнение формы
#         print("Заполняем форму...")
#         address_input = browser.find_element(By.ID, "address")
#         address_input.send_keys("ул. Примерная, д. 123")
#
#         # Выбор способа оплаты
#         print("Выбираем способ оплаты...")
#         payment_option = browser.find_element(By.CSS_SELECTOR, "#payment option[value='card']")
#         payment_option.click()
#
#         # Нажатие кнопки "Подтвердить заказ"
#         print("Нажимаем кнопку 'Подтвердить заказ'...")
#         submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-order")))
#         submit_button.click()
#
#         # Ожидание появления спиннера
#         print("Ожидаем появления спиннера...")
#         spinner = wait.until(EC.visibility_of_element_located((By.ID, "spinner")))
#
#         # Ожидание исчезновения спиннера
#         print("Ожидаем исчезновения спиннера...")
#         wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))
#
#         # Ожидание появления модального окна
#         print("Ожидаем появления модального окна...")
#         modal = wait.until(EC.visibility_of_element_located((By.ID, "modal")))
#
#         # Проверка адреса в модальном окне
#         address_confirm = browser.find_element(By.ID, "address-confirm").text
#         print(f"Подтверждаем адрес: {address_confirm}")
#
#         # Нажатие кнопки "Да" в модальном окне
#         print("Нажимаем кнопку 'Да'...")
#         confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "confirm-address")))
#         confirm_button.click()
#
#         # Ожидание исчезновения модального окна
#         print("Ожидаем исчезновения модального окна...")
#         wait.until(EC.invisibility_of_element_located((By.ID, "modal")))
#
#         # Ожидание появления кнопки "Получить код подтверждения"
#         print("Ожидаем появления кнопки 'Получить код подтверждения'...")
#         get_code_button = wait.until(EC.visibility_of_element_located((By.ID, "get-code")))
#
#         # Нажатие кнопки "Получить код подтверждения"
#         print("Нажимаем кнопку 'Получить код подтверждения'...")
#         get_code_button.click()
#
#         # Ожидание появления результата
#         print("Ожидаем появления результата...")
#         result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
#
#         # Получение пароля
#         password = result.text
#         print(f"Получен пароль: {password}")
#
#         # Небольшая пауза, чтобы увидеть результат
#         time.sleep(3)
#
#         print("Тест успешно завершен!")
#
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#






# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.7.1/index.html"
# with Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 30)
#     driver.find_element("id", "address").send_keys("testing@gmail.com")
#     driver.find_element("css selector", "#payment>option:nth-child(2)").click()
#     driver.find_element("id", "submit-order").click()
#     waiter.until(ec.visibility_of_element_located(("id", "confirm-address"))).click()
#     waiter.until(ec.element_to_be_clickable(("id", "get-code"))).click()
#     result = driver.find_element("id", "result").text
#     print("Result is:", result)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import Keys
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.7.1/index.html")
#     browser.find_element(By.ID, "address").send_keys("Test5")
#     browser.find_element(By.CSS_SELECTOR, ('[value="card"]')).click()
#     browser.find_element(By.CSS_SELECTOR, ("#submit-order")).click()
#     WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
#     )
#     browser.find_element(By.CSS_SELECTOR, "#confirm-address").click()
#     WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "#get-code"))
#     )
#     browser.find_element(By.CSS_SELECTOR, ("#get-code")).click()
#     print(browser.find_element(By.CSS_SELECTOR, ("#result")).text)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.7.1/index.html")
#     browser.find_element(By.ID, 'address').send_keys('Address')
#
#     Select(browser.find_element(By.ID, 'payment')).select_by_value('card')
#     browser.find_element(By.ID, 'submit-order').click()
#
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.element_to_be_clickable((By.ID, 'confirm-address'))).click()
#     wait.until(EC.element_to_be_clickable((By.ID, 'get-code'))).click()
#
#     print(wait.until(EC.visibility_of(browser.find_element(By.ID, 'result'))).text)





