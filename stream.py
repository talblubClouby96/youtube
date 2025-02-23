import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")
options.add_argument('--start-maximized')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

driver = uc.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.youtube.com/")

time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, '//*[@aria-label="Sign in"]')
sign_in_button.click()

email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys("nguyenbaolamrsf3t8fjfdih@dfphayy.us")  
email_field.send_keys(Keys.RETURN)

time.sleep(10)

password_field = driver.find_element(By.XPATH, '//*[@name="Passwd"]') 
password_field.send_keys("Phan9999")  
password_field.send_keys(Keys.RETURN)
time.sleep(100)  

cookies = driver.get_cookies()
# Lưu cookies vào file
with open("cookies/cookies.json", "w") as file:
    json.dump(cookies, file)

print("Cookies đã được lưu thành công vào 'cookies.json'")

driver.quit()

