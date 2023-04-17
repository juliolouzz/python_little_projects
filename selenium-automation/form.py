from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# These two lines under only work if chrome is not open --> to logo into your Google account
options.add_argument(r'--user-data-dir=C:\Users\Julio PC\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Julio")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Louzano")

email = driver.find_element(By.NAME, "email")
email.send_keys("julio.louzano@email.com")

sing_up_btn = driver.find_element(By.XPATH, "/html/body/form/button")
sing_up_btn.click()
