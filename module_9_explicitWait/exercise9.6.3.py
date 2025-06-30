from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')

    wait = WebDriverWait(browser, 20)
    loc_image = (By.ID, 'main-image')
    loc_password = (By.ID, 'password-section')
    atribute_name = 'src'
    exp_status = 'success'

    try:
        wait.until(EC.text_to_be_present_in_element_attribute(loc_image, atribute_name, exp_status))
    except TimeoutException:
        print('TimeoutException_1')


    browser.find_element(*loc_image).click()

    try:
        print(wait.until(EC.visibility_of_element_located(loc_password)).text)
    except TimeoutException:
        print('TimeoutException_2')


# ARC-R34CT0R-P0W3R


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL = "https://parsinger.ru/selenium/9/9.6.3/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     waiter = WebDriverWait(driver, 20)
#     mask = ("id", "main-image")
#     try:
#         waiter.until(ec.text_to_be_present_in_element_attribute(mask, "src", "success"))
#         driver.find_element(*mask).click()
#         result = waiter.until(ec.visibility_of_element_located(("id", "password"))).text
#         print("Result is:", result)
#     except:
#         print("Try again!")



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# with webdriver.Chrome() as browser:
#     url = "https://parsinger.ru/selenium/9/9.6.3/index.html"
#     browser.get(url)
#     locator = (By.ID, "main-image")
#     a = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element_attribute(locator, "src", "success"))
#     headbutton = browser.find_element(*locator)
#     headbutton.click()
#     password = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "password")))
#     print(password.text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/selenium/9/9.6.3/index.html")
#     WebDriverWait(browser, 30).until(
#         EC.text_to_be_present_in_element_attribute(
#             (By.ID, "main-image"), "src", "success"
#         )
#     )
#     browser.find_element(By.ID, "main-image").click()
#     print(
#         WebDriverWait(browser, 10)
#         .until(EC.visibility_of_element_located((By.ID, "password-section")))
#         .text.split(": ")[1]
#     )






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')
#     element = WebDriverWait(browser, 50).until(
#         EC.text_to_be_present_in_element_attribute((By.ID,'main-image'),'src', 'success'))
#
#     browser.find_element(By.ID,'main-image').click()
#     psdw = WebDriverWait(browser,10).until(
#         EC.visibility_of_element_located((By.ID, 'password-section'))
#     )
#
#     print(psdw.text)