import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    elements = browser.find_elements(By.CSS_SELECTOR, "div[style*='background-color']")
    for element in elements:
        color = element.find_element(By.CSS_SELECTOR, 'span').text
        element.find_element(By.CSS_SELECTOR, 'select').click()
        time.sleep(0.5)
        element.find_element(By.XPATH, f".//option[text()='{color}']").click()
        element.find_element(By.CSS_SELECTOR, f"button[data-hex='{color}']").click()
        element.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        element.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(color)
        element.find_element(By.XPATH, ".//button[text()='Проверить']").click()
    browser.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
    time.sleep(5)
    print(browser.switch_to.alert.text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
#     for parent in browser.find_elements(By.CSS_SELECTOR, '#main-container>div'):
#         hex_color = parent.find_element(By.TAG_NAME, 'span').text
#         parent.find_element(By.TAG_NAME, 'select').send_keys(hex_color)
#         parent.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]').click()
#         parent.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
#         parent.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(hex_color)
#         parent.find_element(By.XPATH, "//*[contains(text(), 'Проверить')]").click()
#     browser.find_element(By.XPATH, "//*[contains(text(), 'Проверить все элементы')]").click()
#     print(browser.switch_to.alert.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/5.5/5/1.html")
#
#     for div in browser.find_elements(By.CSS_SELECTOR, "[id='main-container'] > div"):
#         span = div.find_element(By.TAG_NAME, "span").text
#         div.find_element(By.TAG_NAME, "select").send_keys(span)
#         div.find_element(By.XPATH, f"./div/button[@data-hex='{span}']").click()
#         div.find_element(By.XPATH, "./input[@type='checkbox']").click()
#         div.find_element(By.XPATH, "./input[@type='text']").send_keys(span)
#         div.find_element(By.XPATH, "./button").click()
#     browser.find_element(By.CSS_SELECTOR, "body > button").click()
#
#     print(browser.switch_to.alert.text)




#  через Select от Хошева

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
#
#
# with webdriver.Chrome() as driver:
#     driver.get("https://parsinger.ru/selenium/5.5/5/1.html")
#     wait = WebDriverWait(driver, 10)
#     containers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[style*="background-color"]')))
#     for container in containers:
#         # Получаем HEX цвет из <span>
#         hex_color = container.find_element(By.TAG_NAME, 'span').text
#
#         # Выбираем соответствующий цвет в выпадающем списке
#         Select(container.find_element(By.TAG_NAME, 'select')).select_by_value(hex_color)
#
#         # Нажимаем на кнопку с атрибутом data-hex равным HEX цвету
#         container.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]').click()
#
#         # Ставим галочку в чек-боксе
#         container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
#
#         # Вставляем HEX-цвет в текстовое поле
#         container.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(hex_color)
#
#         # Нажимаем кнопку "Проверить"
#         container.find_element(By.XPATH, './/button[text()="Проверить"]').click()
#
#     # Нажимаем кнопку "Проверить все элементы" внизу страницы
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Проверить все элементы"]'))).click()
#
#     # Ждем появления алерт-окна и получаем текст из него
#     alert = wait.until(EC.alert_is_present())
#     alert_text = alert.text
#     alert.accept()
#
#     # Извлекаем числовой код из текста алерта
#     secret_code = ''.join(filter(str.isdigit, alert_text))
#
# print(f'Секретный код: {secret_code}')






import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# url = 'https://parsinger.ru/selenium/5.5/5/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     div_id = browser.find_element(By.ID, 'main-container')
#     div_styles = div_id.find_elements(By.CSS_SELECTOR,'div[style]')
#     for div in div_styles:
#         code_color = div.find_element(By.TAG_NAME,'span').text
#         options = div.find_elements(By.TAG_NAME,'option')
#
#         for i in options:
#             if code_color == i.text:
#                 i.click()
#                 break
#
#         btns = div.find_elements(By.CSS_SELECTOR, 'button[style]')
#         for j in btns:
#             if j.get_attribute('data-hex') == code_color:
#                 j.click()
#                 break
#
#         checkbox = div.find_element(By.CSS_SELECTOR,'input').click()
#         input_text = div.find_element(By.CSS_SELECTOR, 'input[type=text]').send_keys(code_color)
#         btn_check = div.find_element(By.CSS_SELECTOR, '#main-container > div > button').click()
#
#     btn_check_all = browser.find_element(By.XPATH,'/html/body/button').click()
#     alert = browser.switch_to.alert.text
#     print(alert)





# for div in browser.find_elements(By.XPATH, '//div[@id="main-container"]/div'):
#     color = div.find_element(By.TAG_NAME, 'span').text
#     select = Select(div.find_element(By.TAG_NAME, "select"))
#     select.select_by_visible_text(color)
#     div.find_element(By.XPATH, f'div/button[@data-hex="{color}"]').click()
#     div.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
#     div.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(color)
#     div.find_element(By.XPATH, "div/button[text()='Проверить']").click()
# browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
# print(browser.switch_to.alert.text)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
#     elements = browser.find_elements(By.XPATH, '//*[@id="main-container"]/div')
#     for elem in elements:
#         span = elem.find_element(By.TAG_NAME, 'span').text
#         elem.find_element(By.CSS_SELECTOR, f'[value="{span}"]').click()
#         elem.find_element(By.CSS_SELECTOR, f'[data-hex="{span}"]').click()
#         inputs = elem.find_elements(By.TAG_NAME, 'input')
#         inputs[0].click()
#         inputs[1].send_keys(span)
#         elem.find_elements(By.TAG_NAME, 'button')[-1].click()
#     browser.find_element(By.XPATH, '//body/button').click()
#     time.sleep(30)