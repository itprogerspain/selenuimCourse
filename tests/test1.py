from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('http://stepik.org/a/104774')
time.sleep(7)
browser.quit()