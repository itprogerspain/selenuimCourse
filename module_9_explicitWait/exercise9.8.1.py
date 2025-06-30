from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    wait = WebDriverWait(browser, 50)

    wait.until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    wait.until(EC.title_is('345FDG3245SFD'))
    print(browser.find_element(By.ID, 'result').text)





# with webdriver.Chrome(options=options_chrome) as browser:
#     browser.get(url)
#     wait = WebDriverWait(browser,timeout=60)
#     wait.until(EC.element_to_be_clickable((By.ID,'btn'))).click()
#     wait.until(lambda browser: browser.title == '345FDG3245SFD')
#     print(browser.find_element(By.ID,'result').text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/expectations/3/index.html')
#     wait = WebDriverWait(browser, 30)
#     wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
#     wait.until(EC.title_contains('345FDG3245SFD'))
#     print(browser.find_element(By.ID, 'result').text)