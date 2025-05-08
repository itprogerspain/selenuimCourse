import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    expression = browser.find_element(By.ID, "text_box")
    number = eval(expression.text)

    browser.find_element(By.ID, "selectId").click()

    all_options = browser.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if option.text == str(number):
            option.click()

    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, "result").text)
    time.sleep(5)







import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/6/6.html')

    # Находим выражение и считаем
    expression = browser.find_element(By.ID, 'text_box')
    number = eval(expression.text)

    # Отправляем результат в select через send_keys
    select = browser.find_element(By.ID, 'selectId')
    select.send_keys(str(number))

    # Кликаем по кнопке
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # Выводим результат
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)







from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/6/6.html')
    equation = browser.find_elements('id', 'text_box')
    eq = (i.text for i in equation)
    eq = eval(*eq)

    browser.find_element('id', 'selectId').send_keys(eq)
    browser.find_element('class name', 'btn').click()
    print(browser.find_element('id', 'result').text)