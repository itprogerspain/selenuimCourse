import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    data = ['Мария', 'Виноградова', 'Александровна', '25', 'Москва', 'selenium@selenium.com']
    for input_form, value in zip(input_forms, data):
        input_form.send_keys(value)
    browser.find_element(By.ID, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# URL = "https://parsinger.ru/selenium/1/1.html"
# data = ["Иванов", "Иван", "Иванович", 30, "Иваново", "ivanov@ivan.ru"]
#
# def filling_forms(url: str):
#     with webdriver.Chrome() as driver:
#         driver.get(url)
#         input_form = driver.find_elements(By.CLASS_NAME, "form")
#         for d, f in enumerate(input_form):
#             f.send_keys(data[d])
#         driver.find_element(By.ID, "btn").click()
#         print(driver.find_element(By.ID, "result").text)
#
# filling_forms(URL)




# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/1/1.html')
#     fields = ['first_name', 'last_name', 'patronymic', 'age', 'city', 'email']
#     for field in fields:
#         browser.find_element(By.XPATH, '//input[@name="' + field + '"]').send_keys(field.upper())
#     browser.find_element(By.ID, 'btn').click()
#     pyperclip.copy(browser.find_element(By.ID, 'result').text)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# url = 'http://parsinger.ru/selenium/1/1.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for field in browser.find_elements(By.CLASS_NAME, 'form'):
#         field.send_keys('Text')
#     browser.find_element(By.ID, 'btn').click()
#     input()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# data = ['Петров', 'Петр', 'Петрович', 35, 'Минск', 'petr25cm@mamba.ru']
# url = 'https://parsinger.ru/selenium/1/1.html'
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     form = browser.find_elements(By.CLASS_NAME, 'form')
#     for i in range(len(data)):
#         form[i].send_keys(data[i])
#     browser.find_element(By.ID, 'btn').click()
#     answer = browser.find_element(By.ID, 'result').text
#     print(answer)


