from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

page_title = driver.title
current_url = driver.current_url
page_source = driver.page_source

print(f"Title of the webpage: {page_title}")
print(f"Current URL: {current_url}")

with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

driver.quit()
