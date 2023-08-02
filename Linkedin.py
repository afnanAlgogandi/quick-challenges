from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



# Create a new Firefox browser instance
browser = webdriver.Firefox()

# Navigate to the LinkedIn website
browser.get("https://www.linkedin.com/login")
sleep(3)

email_field = browser.find_element(value="username")
email_field.send_keys("Your_Email")

password_field = browser.find_element(value="password")
password_field.send_keys("Your_Password")

password_field.send_keys(Keys.RETURN)

# Wait for the home page to load
sleep(30)

browser.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
sleep(10)
browser.find_element(By.ID,value="ember34").click()
sleep(3)
browser.find_element(By.ID, "ember89").click()


