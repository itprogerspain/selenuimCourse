from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
URL = "https://bot.sannysoft.com"

with webdriver.Chrome(options=options) as browser:
    browser.get(URL)
    time.sleep(20)
    # filename = "full_page.png"
    # total_width = browser.execute_script("return document.documentElement.scrollWidth")
    # total_height = browser.execute_script("return document.documentElement.scrollHeight")
    # browser.set_window_size(total_width, total_height)
    # browser.save_screenshot(filename)