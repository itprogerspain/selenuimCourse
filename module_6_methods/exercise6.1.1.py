import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Страница 2').click()
    time.sleep(1)
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Перейти на страницу 3').click()
    time.sleep(1)
    browser.back()
    time.sleep(1)
    browser.back()
    time.sleep(1)
    my_password = browser.find_element(By.ID, 'getPasswordBtn').click()
    time.sleep(6)



# driver.get('https://parsinger.ru/selenium/6/6.2/index.html')
# driver.find_element('xpath', '//a[contains(@href, "page2")]').click()
# driver.find_element('xpath', '//a[contains(@href, "page3")]').click()
# for i in range(2):
#     driver.back()
# driver.find_element('xpath', '//button[@id="getPasswordBtn"]').click()
# ans = driver.switch_to.alert.text
# print(ans)

