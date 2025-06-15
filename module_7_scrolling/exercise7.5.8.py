from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.common.by import By
import time

count = 0

with Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.5/index.html")
    action = ActionChains(browser)
    action.send_keys(Keys.TAB).pause(0.2).perform()
    for _ in range(20):
        action.send_keys(Keys.END).pause(0.6).perform()

    action.send_keys(Keys.HOME).pause(0.1).perform()
    users = browser.find_elements(By.CLASS_NAME, 'card')
    for user in users:
        like_containers = user.find_elements(By.CLASS_NAME, 'like-container')
        for like_container in like_containers:
            like_container.find_element(By.CLASS_NAME, 'like-btn').click()
            time.sleep(0.1)
    numbers = browser.find_elements(By.CLASS_NAME, 'big-number')
    for number in numbers:
        count += int(number.text)
    print(count)




# from selenium.webdriver import Chrome, ActionChains, Keys
#
# URL = "https://parsinger.ru/selenium/7/7.5/index.html"
# result = []
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     main_container = driver.find_element("id", "container")
#     for _ in range(20):
#         action.send_keys_to_element(main_container, Keys.END).pause(0.1).perform()
#     boxes = driver.find_elements("class name", "like-container")
#     for box in boxes:
#         box.find_element("class name", "like-btn").click()
#         num = int(box.find_element("class name", "big-number").text)
#         result.append(num)
#     print("Result is:", sum(result))




# by Miroshnichenko

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# url = "https://parsinger.ru/selenium/7/7.5/index.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(1)  # Даём странице загрузиться
#     container = browser.find_element(By.ID, "container")
#
#     num_count = 0
#     proceed_count = 0
#     last_card_count = 0  # Количество карточек перед скроллом
#
#     while True:
#         # Получаем карточки и кнопки лайков заново после каждого скролла
#         cards = browser.find_elements(By.CLASS_NAME, "card")
#         like_buttons = [card.find_element(By.CLASS_NAME, "like-btn") for card in cards]
#
#         # Лайкаем только новые карточки
#         for i in range(proceed_count, len(like_buttons)):
#             like_buttons[i].click()  # Кликаем
#
#         # Считаем числа
#         numbers = browser.find_elements(By.CLASS_NAME, "big-number")
#         for i in range(proceed_count, len(numbers)):
#             num_count += int(numbers[i].text)  # Добавляем число в общий счёт
#
#         # Обновляем `proceed_count` перед скроллом
#         proceed_count = len(cards)
#
#         # Запоминаем количество карточек перед скроллом
#         last_card_count = proceed_count
#
#         # Скроллим вниз
#         browser.execute_script("arguments[0].scrollBy(0, 600);", container)
#         time.sleep(1)  # Даём контенту подгрузиться
#
#         # Получаем количество карточек после скролла
#         new_card_count = len(browser.find_elements(By.CLASS_NAME, "card"))
#
#         # Если карточек не прибавилось – конец контейнера
#         if new_card_count == last_card_count:
#             print("Достигнут конец контейнера, скрипт завершён!")
#             break
#
#     print(f"Общее число лайков: {num_count}")


# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/7/7.5/index.html')
#     container = browser.find_element(By.ID, 'container')
#     k = 0
#     while len(btns := browser.find_elements(By.CLASS_NAME, 'like-btn')) != k:
#         for btn in btns[k:]:
#             btn.click()
#         container.send_keys(Keys.ARROW_DOWN)
#         time.sleep(.2)
#         k = len(btns)
#
#     print(sum(map(lambda n: int(n.text), browser.find_elements(By.CLASS_NAME, 'big-number'))))




# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.5/index.html")
#     actions = ActionChains(browser)
#     scroll=browser.find_element(By.ID,'container')
#     old = 0
#     while True:
#         scroll.send_keys(Keys.END)
#         time.sleep(0.5)
#         new = len(browser.find_elements(By.CSS_SELECTOR, '.card'))
#         if new==old:
#             break
#         old = new
#
#     cards = browser.find_elements(By.CSS_SELECTOR, ".card")
#     total=0
#     for card in cards:
#         card.find_element(By.CLASS_NAME,'like-btn').click()
#         total+=int(card.find_element(By.CLASS_NAME,'big-number').text)
#
#     print(total)



#By Zanzara
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# total = 0
#
# with webdriver.Firefox() as browser:
#     browser.get("https://parsinger.ru/selenium/7/7.5/index.html")
#     time.sleep(5)
#     old_len = 0
#     while len((cards := browser.find_elements(By.CLASS_NAME, "like-container"))) != old_len:
#         old_len = len(cards)
#         browser.execute_script("arguments[0].scrollIntoView(true);", cards[-1])
#         time.sleep(.1)
#     print(f'cards in total = {len(cards)}')
#
#     for card in cards:
#         browser.execute_script("arguments[0].scrollIntoView(true);", card)
#         card.find_element(By.CLASS_NAME, "like-btn").click()
#         total += int(card.find_element(By.CLASS_NAME, "big-number").text)
#         time.sleep(.1)
#
#     print(total)