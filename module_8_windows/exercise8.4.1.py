from selenium import webdriver
from selenium.webdriver.common.by import By
import re


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')
    iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe_element)
    iframe_content = browser.page_source
    res = re.findall(r'\*(.*?)\*', iframe_content)
    print(res)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import re
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/8/8.4.1/")
#     frame = browser.find_element(By.TAG_NAME, 'iframe')
#     browser.switch_to.frame(frame)
#     print(''.join(re.findall( r'\*(.)\*', browser.page_source)))



# from selenium import webdriver
# import re
#
# URL = "https://parsinger.ru/selenium/8/8.4.1/"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     iframe = driver.find_element("tag name", "iframe")
#     driver.switch_to.frame(iframe)
#     text_source = driver.page_source
#     words = re.findall("\*\w\*", text_source)
#     result = "".join(words).replace("*", "")
#     print("Result is:", result)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.1/')
#
#     # Переключаемся на iframe
#     iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
#     browser.switch_to.frame(iframe_element)
#
#     # Извлекаем HTML содержимое из iframe
#     iframe_content = [i.split('*')[1] for i in browser.page_source.split() if '*' in i]
#     iframe_content = ''.join(iframe_content)
#     print(iframe_content)





# from selenium.webdriver.common.by import By
#
# from selenium_scripts.browser_setup import browser
#
# with browser:
#     browser.get('https://parsinger.ru/selenium/8/8.4.1/')
#
#     browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, 'iframe'))
#     text = browser.page_source
#
#     letters = []
#
#     words = text.split()
#     for word in words:
#         if '*' in word:
#             for i in range(len(word)):
#                 if i != 0:
#                     if word[i - 1] == '*':
#                         if i != len(word) - 1:
#                             if word[i + 1] == '*':
#                                 letters.append(word[i])
#
# print(''.join(letters))
