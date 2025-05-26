import time
from os import times_result

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/7/7.2/example_keys/index.html")
    time.sleep(1)
    # Находим поле
    input_field_1 = browser.find_element(By.ID, "field1")
    input_field_1.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
    input_field_1.send_keys(Keys.DELETE)  # Удалить выделенное
    input_field_1.send_keys(Keys.TAB)
    time.sleep(5)
    input_field_2 = browser.find_element(By.ID, "field2")
    input_field_2.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
    input_field_2.send_keys(Keys.DELETE)  # Удалить выделенное
    input_field_2.send_keys(Keys.TAB)

    input_field_3 = browser.find_element(By.ID, "field3")
    input_field_3.clear()
    input_field_3.send_keys('Keys.TAB')
    input_field_3.send_keys(Keys.TAB)
    time.sleep(3)
    browser.send_keys('2023-05-19')


# либо второй вариант используя ActionChains:

# # Вариант 1: С предварительным фокусом
# input_field.click()  # Фокус на элементе
# ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
#
# # Вариант 2: Включая элемент в цепочку
# ActionChains(browser).click(input_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()