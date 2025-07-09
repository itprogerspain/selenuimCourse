from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    wait = WebDriverWait(browser, 15)

    code = []

    buttons = browser.find_elements(By.CLASS_NAME, 'box_button')
    for button in buttons:
        button.click()
        wait.until(EC.element_to_be_clickable((By.ID, 'close_ad'))).click()
        wait.until(EC.invisibility_of_element_located((By.ID, 'close_ad')))
        wait.until(lambda driver: button.text.strip() != '')
        code.append(button.text)
        final_result = '-'.join(code)
    print(final_result)



# F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120




# from selenium.webdriver import Chrome
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/5.9/5/index.html"
# codes = []
# with Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 30)
#     boxes = driver.find_elements("class name", "box_button")
#     for box in boxes:
#         waiter.until(ec.element_to_be_clickable(box)).click()
#         driver.find_element("id", "close_ad").click()
#         waiter.until(lambda _: box.text != "")
#         codes.append(box.text)
#     print("Result is:", "-".join(codes))



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# list = []
#
# with webdriver.Chrome() as browser:
#     weit = WebDriverWait(browser, 10)
#     browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
#     data_index = browser.find_elements(By.CLASS_NAME, 'box_button')
#     for i in data_index:
#         index = int(i.get_attribute('data-index'))
#         #клик по квадратику когда он доступен
#         weit.until(EC.element_to_be_clickable((By.XPATH, f'.//div[@data-index = {index}]'))).click()
#         #клик по крестику когда он доступен
#         weit.until(EC.element_to_be_clickable((By.ID, 'close_ad'))).click()
#         #реклама ушла
#         weit.until(EC.text_to_be_present_in_element_attribute((By.ID, 'ad_window'), 'style', 'display: none; opacity: 1;'))
#         list.append(i.text)
#     print('-'.join(x for x in list))




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.9/5/index.html")
#     result = []
#     for btn in browser.find_elements(By.CSS_SELECTOR, ".box_button"):
#         btn.click()
#         WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#close_ad"))).click()
#         while not btn.text:
#             pass
#         result.append(btn.text)
#     print("-".join(result))




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = 'https://parsinger.ru/selenium/5.9/5/index.html'
#
#
# with webdriver.Chrome() as browser:
#     browser.get(url=url)
#     wait = WebDriverWait(browser, 20)
#
#     buttons = browser.find_elements(By.CLASS_NAME, "box_button")
#     ad_window = (By.ID, "ad_window")
#     close_ad_button = (By.ID, "close_ad")
#
#     for button in buttons:
#         button.click()
#         wait.until(EC.element_to_be_clickable(close_ad_button)).click()
#         wait.until(EC.invisibility_of_element_located(ad_window))
#         wait.until(lambda _: button.text)
#
#     print('-'.join(button.text for button in buttons))


