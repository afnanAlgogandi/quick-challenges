from linkedin_auto_message_sender_bot import *
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/login')

# entering username
username = driver.find_element(By.ID, "username")
# Enter Your Email Address
username.send_keys('')


# Entering password
pword = driver.find_element(By.ID,"password")
# Enter Your Password
pword.send_keys("")
# Click the login button
driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button").click()
time.sleep(10)

# Navigate to the LinkedIn login page
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')

driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/ul/li[1]/div/div[2]/button').click()
time.sleep(20)


driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
time.sleep(50)


#try to unconnect to all request
#for n in find_element(By.CLASS_NAME, "artdeco-button__text"):
#   driverfind_element(By.NAME, "سحب").click()
#   time.sleep(10)

#time.sleep(20)

