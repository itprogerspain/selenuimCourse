from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/4/index.html')
    time.sleep(1)
    wait = WebDriverWait(browser, 15)
    actions = ActionChains(browser)
    # time.sleep(60)
    word = browser.find_element(By.ID, "target-word").text
    letters = browser.find_elements(By.CLASS_NAME, "draggable-letter")
    targets = browser.find_elements(By.CLASS_NAME, "letter-slot")

    for index, char in enumerate(word):
        for letter in letters:
            if char == letter.text:
                target = targets[index]
                actions.click_and_hold(letter).move_to_element(target).release().perform()
    wait.until(lambda driver: browser.find_element(By.ID, 'password').text.strip() != '')
    print(browser.find_element(By.ID, 'password').text)



# 0000-MAGIC-WORD-0000





# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# URL = "https://parsinger.ru/draganddrop/4/index.html"
#
# with webdriver.Chrome() as browser:
#     browser.get(URL)
#     target_word_element = WebDriverWait(browser, 10).until(
#                 EC.visibility_of_element_located((By.ID, "target-word")))
#     target_word = target_word_element.text
#     actions = ActionChains(browser)
#
#     for index, letter in enumerate(target_word):
#         source_letter_xpath = f"//div[text()='{letter}']"
#         source_element = WebDriverWait(browser, 5).until(
#                     EC.presence_of_element_located((By.XPATH, source_letter_xpath)))
#
#         target_slot_xpath = f"//div[@data-index='{index}']"
#         target_element = WebDriverWait(browser, 5).until(
#             EC.presence_of_element_located((By.XPATH, target_slot_xpath))
#         )
#
#         actions.drag_and_drop(source_element, target_element).perform()
#
#     password_element = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.ID, "password"))
#     )
#     password_text = password_element.text
#     time.sleep(.2)
#     print(password_text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.page_load_strategy = "eager"
# options.add_argument("--headless")
#
# with webdriver.Chrome(options=options) as browser:
#     browser.get("https://parsinger.ru/draganddrop/4/index.html")
#     letters_elems = dict(map(lambda elem: (elem.text, elem), browser.find_elements(By.CLASS_NAME, 'draggable-letter')))
#     word = browser.find_element(By.ID, 'target-word').text
#     slots = browser.find_elements(By.CLASS_NAME, 'letter-slot')
#     action = webdriver.ActionChains(browser)
#
#     for letter, slot in zip(word, slots):
#         action.drag_and_drop(letters_elems[letter], slot).perform()
#
#     print(browser.find_element(By.ID, 'password').text)






# from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = "https://parsinger.ru/draganddrop/4/index.html"
#
# def get_letter_webelement(letter):
#     letters = driver.find_elements("class name", "draggable-letter")
#     for item in letters:
#         if item.text == letter:
#             return item
#
# with Chrome() as driver:
#     driver.get(url=URL)
#     action = ActionChains(driver)
#     word = driver.find_element("id", "target-word").text
#     slots = driver.find_elements("class name", "letter-slot")
#     for i in range(len(word)):
#         action.drag_and_drop(get_letter_webelement(word[i]), slots[i]).perform()
#     result = driver.find_element("id", "password").text
#     print("Result is:", result)