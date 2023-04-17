from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(r'--user-data-dir=C:\Users\Julio PC\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles_english = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(total_articles_english.text)
# total_articles_english.click()

English = driver.find_element(By.LINK_TEXT, "English")
# English.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)



