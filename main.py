import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

username = "user"
password = "password"

# Driver
driver = webdriver.Chrome()
driver.get("facebook")

# Find Elements
someElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/h2/a")
userElement= driver.find_element_by_id("email")
passElement = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")

# Enter Elements
userElement.send_keys(username)
passElement.send_keys(password)
submit.click()

# Wait & Validate
wait = WebDriverWait( driver, 5 )
page_title = driver.title

if (page_title == "Facebook"):
    print('Pass')
else:
    print("Fail")

driver.send_keys(Keys.RETURN)
driver.close()



