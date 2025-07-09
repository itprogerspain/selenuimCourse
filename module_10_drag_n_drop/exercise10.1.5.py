from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    elements = browser.find_elements(By.CLASS_NAME, "draganddrop")
    targets = browser.find_elements(By.CLASS_NAME, "draganddrop_end")
    for element, target in zip(elements, targets):
        actions.click_and_hold(element).move_to_element(target).release().perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# F934-3902-2FH4-DV02-3454-9HCX-4F53-12FS




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = "https://parsinger.ru/selenium/5.10/3/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     blocks_start = driver.find_elements("class name", "draganddrop")
#     blocks_end = driver.find_elements("class name", "draganddrop_end")
#     for i in range(len(blocks_start)):
#         action.drag_and_drop(blocks_start[i], blocks_end[i]).perform()
#     print("Result is:", driver.find_element("id", "message").text)




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.color import Color
#
# URL = "https://parsinger.ru/selenium/5.10/3/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     blocks_start = sorted(driver.find_elements("class name", "draganddrop"), key=lambda x: Color.from_string(x.value_of_css_property("background-color")).hex)
#     blocks_end = sorted(driver.find_elements("class name", "draganddrop_end"), key=lambda x: Color.from_string(x.value_of_css_property("border-color")).hex)
#     for i in range(len(blocks_start)):
#         action.drag_and_drop(blocks_start[i], blocks_end[i]).perform()
#     print("Result is:", driver.find_element("id", "message").text)




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import time
#
# url = "https://parsinger.ru/selenium/5.10/3/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     time.sleep(2)  # Даем странице время для загрузки
#
#     draganddrops = driver.find_elements(By.CSS_SELECTOR, ".draganddrop.ui-draggable")
#     draganddrop_ends = driver.find_elements(By.CSS_SELECTOR, ".draganddrop_end")
#
#     for draganddrop in draganddrops:
#         color = draganddrop.value_of_css_property("background-color")
#         target = None
#         for end in draganddrop_ends:
#             border_color = end.value_of_css_property("border-top-color")
#             if color == border_color:
#                 target = end
#                 break
#
#         if target:
#             ActionChains(driver).drag_and_drop(draganddrop, target).perform()
#             time.sleep(0.5)  # Даем время для обработки действия
#
#     time.sleep(2)  # Даем время для появления сообщения
#     message = driver.find_element(By.ID, "message").text
#     print("Сообщение:", message)




# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.color import Color
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
#
#
# def get_color(item: WebElement, type_color: str) -> str:
#     color_rgb = Color.from_string(item.value_of_css_property(f'{type_color}-color')).rgb
#     return color_rgb
#
#
# url = "https://parsinger.ru/selenium/5.10/3/index.html"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--force-device-scale-factor=0.5")
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     actions = ActionChains(browser)
#
#     end_boxes = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')
#     targets = {get_color(x, 'border'): x for x in end_boxes}
#
#     boxes = browser.find_elements(By.CLASS_NAME, 'draganddrop')
#     for box in boxes:
#         color = get_color(box, 'background')
#         target = targets[color]
#         actions.drag_and_drop(box, target).release().perform()
#
#     password = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'message')))
#     print(password.text)
