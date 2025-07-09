from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get('https://parsinger.ru/selenium/5.10/4/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)

    colors = ['red', 'blue', 'green', 'black']

    balls = {color: browser.find_elements(By.CLASS_NAME, f"{color}_ball") for color in colors}
    targets = {color: browser.find_element(By.CLASS_NAME, color) for color in colors}

    for color in colors:
        for ball in balls[color]:
            actions.click_and_hold(ball).move_to_element(targets[color]).release().perform()

    wait.until(lambda driver: browser.find_element(By.ID, 'message').text.strip() != '')
    print(browser.find_element(By.ID, 'message').text)



# ER96-SVN0-34HX-ER3W-WHJ5-WHG4-SNJ1-12LO


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as driver:
#     browser.maximize_window()
#     driver.get("https://parsinger.ru/selenium/5.10/4/index.html")
#
#     driver.implicitly_wait(10)
#
#     balls = driver.find_elements(By.CLASS_NAME, "ball_color")
#     baskets = {color: driver.find_element(By.CSS_SELECTOR, f".basket_color.{color}") for color in
#                ["red", "blue", "green", "black"]}
#
#     for ball in balls:
#         color = ball.get_attribute("class").split(" ")[1].replace("_ball", "")
#         basket = baskets[color]
#
#         ActionChains(driver).drag_and_drop(ball, basket).perform()
#
#         time.sleep(0.1)  # небольшая задержка для более плавного перемещения
#
#     message = driver.find_element(By.CLASS_NAME, "message").text
#     print(message)



# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# URL = "https://parsinger.ru/selenium/5.10/4/index.html"
#
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     time.sleep(2)
#     balls = driver.find_elements("class name", "ball_color")
#     baskets = driver.find_elements("class name", "basket_color")
#     for ball in balls:
#         color_ball = ball.value_of_css_property("background-color")
#         for basket in baskets:
#             color_basket = basket.value_of_css_property("background-color")
#             if color_ball == color_basket:
#                 ActionChains(driver).drag_and_drop(ball, basket).perform()
#     print("Result is:", driver.find_element("class name", "message").text)



# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# url = "https://parsinger.ru/selenium/5.10/4/index.html"
# opt = webdriver.ChromeOptions()
# opt.add_argument('--window-size=1280,720')
#
# with webdriver.Chrome(options=opt) as browser:
#     browser.get(url)
#     sleep(10)
#     action = ActionChains(browser)
#     balls = browser.find_elements(By.CLASS_NAME, 'ball_color')
#     distance = {
#     'black_ball': 850,
#     'red_ball': 250,
#     'blue_ball': 400,
#     'green_ball': 650}
#     for ball in balls:
#         color = ball.get_attribute('class').split(' ')[1]
#         action.drag_and_drop_by_offset(ball, xoffset=distance[color], yoffset=0).perform()
#         sleep(0.5)
#
#     pas = browser.find_element(By.CLASS_NAME, 'message').text
#     print(pas)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--window-size=1920,1080')
#
# with webdriver.Chrome(options=chrome_options) as driver:
#     actions = ActionChains(driver)
#     driver.get('https://parsinger.ru/selenium/5.10/4/index.html')
#
#     colors = ('red', 'blue', 'green', 'black')
#     for color in colors:
#         balls = driver.find_elements(By.CLASS_NAME, f'{color}_ball')
#         field = driver.find_element(By.CLASS_NAME, color)
#         for ball in balls:
#             actions.drag_and_drop(ball, field).perform()
#
#     print(driver.find_element(By.CLASS_NAME, 'message').text)



