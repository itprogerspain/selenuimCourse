import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    all_elements = browser.find_elements(By.TAG_NAME, 'p')
    total = sum(int(element.text) for element in all_elements)
    print(total)
    time.sleep(5)




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.html')
#     all_elements = browser.find_elements(By.TAG_NAME, 'p')
#     count = 0
#     for element in all_elements:
#         element_ = int(element.text)
#         count += element_
#     print(count)
#     time.sleep(5)





# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/3/3.html')
#     data_p = browser.find_elements(By.TAG_NAME, 'p')
#     print(sum(map(lambda x: int(x.text), filter(lambda x: x.text.isdigit(), data_p))))