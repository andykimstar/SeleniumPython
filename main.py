import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

email = "ajyk9201@gmail.com"
password = "Starbucks#92"
location = "661 University Ave, Toronto, ON, Canada"

# Driver
driver = webdriver.Chrome()
driver.get("https://www.starbucks.ca/account/signin")

# Find Elements
locationElement = driver.find_element(By.XPATH, "//*[@for='bigsearch-query-location-input']")
searchElement = driver.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']")
locationElement.click()
locationElement.send_keys(city)
locationElement.send_keys(Keys.RETURN)
searchElement.click()
time.sleep(5)


# Step 1. Go to the Starbucks Page & Sign In

## Enter Email
emailElement = driver.find_element(By.XPATH, "//*[@type='email']")
emailElement.click()
emailElement.send_keys(email)

## Enter Password
passwordElement = driver.find_element(By.XPATH, "//*[@type='password']")
passwordElement.click()
passwordElement.send_keys(password)

## Enter Sign In
signinElement = driver.find_element(By.XPATH, "//*[@type='submit']")
signinElement.click()

## Go to  Store Locator
locateElement = driver.find_element(By.XPATH, "//*[@href='/store-locator']")
locateElement.click()

## Find Store
storeElement = driver.find_element(By.XPATH, "//input[@type='search']")
storeElement.click()
storeElement.send_keys(location)

## Enter Store Name
storeStreet = 
storeCity = 
foundStoreElement = driver.find_element(By.XPATH, "//*[contains(text(), f"{storeStreet}") and contains(text(), f"{storeCity}")]")
foundStoreElement = driver.find_element(By.XPATH, "//*[contains(text(), "661 University") and contains(text(), "Toronto")]")

** Make sure its not closed

button[@type='button']

//*[@id="content"]/div/div[2]/section/div[1]/div/div[2]/article[49]/div/div[2]/div[2]/button

# Step 3. Find & enter the Store Location

# Step 4. Select a Drink of choice or randomm
# - Make sure it is not SOLD OUT
# - Conrtol Ice Level

# Step 5. Click 'Add to Order'

# Step 6. Verify the 'Review Order'

# Step 7. Then Check OUT

# Log the Drink & Price to Track

#//button[@data-testid="structured-search-input-search-button"]
#//*[@id="search-tabpanel"]//descendant::button[@testid="structured-search-input-search-button"]
#//*[@id="search-tabpanel"]/div[1]/div[5]/div[1]/div[2]/button

#wait = WebDriverWait(driver, timeout=2)
#wait

#userElement= driver.find_element_by_id("email")
#passElement = driver.find_element_by_id("pass")

#submit = driver.find_element_by_id("loginbutton")
# Enter Elements
#userElement.send_keys(username)
#passElement.send_keys(password)
#submit.click()

# Wait & Validate
#wait = WebDriverWait( driver, 5 )
#page_title = driver.title

#if (page_title == "Facebook"):
#    print('Pass')
#else:
#    print("Fail")

driver.send_keys(Keys.RETURN)
driver.close()



