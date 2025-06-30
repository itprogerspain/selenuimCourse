from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                   'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    wait = WebDriverWait(browser, 50)

    for id in ids_to_find:
        locator = (By.ID, f'{id}')
        wait.until(EC.visibility_of_element_located(locator)).click()

    alert = wait.until(EC.alert_is_present())
    print(browser.switch_to.alert.text)


# CFoCZ3Ze-8CiPCnNB-XuEMunrz-vmlzQ3gH-axhUiw2I-QQK13iyY-j7kD7uIR




# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/5.9/3/index.html"
# ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     for id_to_find in ids_to_find:
#         boxes = WebDriverWait(driver, 100).until(ec.visibility_of_all_elements_located(("id", id_to_find)))
#         for box in boxes:
#             box.click()
#     result = WebDriverWait(driver, 50).until(ec.alert_is_present()).text
#     print("Result is:", result)



# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.9/3/index.html')
#
#     ids_to_find = [
#         'xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
#         'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw',
#         '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR'
#     ]
#
#     for item in ids_to_find:
#         WebDriverWait(driver, 360).until(EC.visibility_of_element_located((By.ID, item))).click()
#         print(f'clicked: {item}')
#
#     print(driver.switch_to.alert.text)





# from selenium.common.exceptions import TimeoutException
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import Keys
# from selenium.webdriver.support.ui import WebDriverWait
#
# ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.9/3/index.html")
#     for id in ids_to_find:
#         while True:
#             try:
#                 WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, id)))
#                 browser.find_element(By.ID,id).click()
#                 break
#             except TimeoutException:
#                 continue
#     alert=browser.switch_to.alert
#     print(alert.text)