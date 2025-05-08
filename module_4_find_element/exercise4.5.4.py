from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    all_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    total = sum(int(element.text) for element in all_elements)
    print(total)




# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('https://stepik-parsing.ru/selenium/3/3.html')
#     print(sum([int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]))






















