import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    stormtroopers = browser.find_elements(By.TAG_NAME, "a")
    count = 0
    for stormtrooper in stormtroopers:
        stormtrooper_ = stormtrooper.get_attribute('stormtrooper')
        try:
            number = int(stormtrooper_)
            count += number
        except ValueError:
            continue
    input_number = browser.find_element(By.ID, "inputNumber")
    input_number.send_keys(count)
    check_button = browser.find_element(By.ID, "checkBtn")
    check_button.click()
    res = browser.find_element(By.ID, "feedbackMessage")
    print(res.text)
    time.sleep(5)



# from selenium import webdriver
#
# URL = "https://parsinger.ru/selenium/3/3.3.3/index.html"
# with webdriver.Chrome() as driver:
#     driver.get(url=URL)
#     stormtroopers = driver.find_elements("tag name", "a")
#     numbers = []
#     for stormtrooper in stormtroopers:
#         attribute = stormtrooper.get_attribute("stormtrooper")
#         if attribute.isdigit():
#             numbers.append(int(attribute))
#     driver.find_element("id", "inputNumber").send_keys(sum(numbers))
#     driver.find_element("id", "checkBtn").click()
#     code = driver.find_element("id", "feedbackMessage").text
#     print("Result is:", code)




# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
#     els = browser.find_elements("tag name", "a")
#     total = 0
#     for el in els:
#         link = el.get_attribute("stormtrooper")
#         if link.isdigit():
#             total += int(link)
#     button1 = browser.find_element("id", "inputNumber")
#     button2 = browser.find_element("id", "checkBtn")
#     button1.send_keys(total)
#     button2.click()
#     result = browser.find_element("id", "feedbackMessage")
#     print(result.text)






# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# count_sum = 0
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
#
#     shtoorms = browser.find_elements(By.LINK_TEXT,'Сколько нас')
#     for shtoorm in shtoorms:
#         x = shtoorm.get_attribute('stormtrooper')
#         if x.isdigit():
#             count_sum += int(x)
#
#     input = browser.find_element(By.ID, 'inputNumber')
#     input.send_keys(count_sum)
#
#     button = browser.find_element(By.ID, 'checkBtn')
#     button.click()
#
#     pswd = browser.find_element(By.ID, 'feedbackMessage').text
#     print(pswd)







# lst = [element.get_attribute("stormtrooper") for element in browser.find_elements(By.TAG_NAME, "a")]
# browser.find_element(By.ID, "inputNumber").send_keys(str(sum(map(int, filter(str.isdigit, lst)))))
# browser.find_element(By.ID, "checkBtn").click()






with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/3/3.3.3/index.html#')

    stormtroopers_counter = sum(
        int(a.get_attribute('stormtrooper')) for a in driver.find_elements(By.TAG_NAME, 'a')
        if a.get_attribute('stormtrooper') and a.get_attribute('stormtrooper').isdigit()
    )

    driver.find_element(By.ID, 'inputNumber').send_keys(str(stormtroopers_counter))
    driver.find_element(By.ID, 'checkBtn').click()

    print(driver.find_element(By.ID, 'feedbackMessage').text)