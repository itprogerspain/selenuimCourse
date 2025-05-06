import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html')
    browser.maximize_window()

    # делает скриншот найденного элемента
    browser.find_element(By.ID, 'this_pic').screenshot('file_name3.png')

    # делает скриншот всей страницы
    # browser.save_screenshot("file_name1.jpg")
    time.sleep(6)






# import time
# import faker
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html')
#     time.sleep(2)
#
#     screen = browser.find_element(By.ID, 'this_pic').screenshot('file.png')
