from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# These two lines under only work if chrome is not open --> to logo into your Google account
options.add_argument(r'--user-data-dir=C:\Users\Julio PC\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

big_cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

total_cookies = driver.find_element(By.CSS_SELECTOR, "#cookies")

cookies_per_second = driver.find_element(By.CSS_SELECTOR, "#cookiesPerSecond")

bot_on = True

time_out = time.time() + 60
while bot_on:
    big_cookie.click()
    if time.time() > time_out:
        break

