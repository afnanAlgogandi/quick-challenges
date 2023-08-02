


# #Using bot_studio
# from bot_studio import *

# message1 = "Hello, this is an automated message sent using Python!,,,,from Mohammed Adel"

# linkedin=bot_studio.linkedin()
# linkedin.login(email="", password='')
# linkedin.send_message(keyword=r'https://www.linkedin.com/in/ibrahem-elnawasany/', message=message1)





# #using selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By





# # linkedin account
# email = 'alhydrym7@gmail.com'
# password = '774390003Mm' 


# # first download  webdriver from https://chromedriver.chromium.org/downloads
# driver = webdriver.Chrome('/Users/ekram/Downloads/chromedriver_mac_arm64/chromedriver')

# try: 
    
#     # sign in page of linkedin
#     driver.get('https://www.linkedin.com/')
    
#     # sign in 
#     driver.find_element(By.CLASS_NAME, 'session_key').send_keys(email)
#     driver.find_element(By.ID, 'session_password').send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, 
#                         '#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form:nth-child(7) > div.flex.justify-between.sign-in-form__footer--full-width > button').click()
            
#     # got to page of Eng.Ibrahem            
#     driver.get('https://www.linkedin.com/in/ibrahem-elnawasany/')
    
#     # follow button
#     driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button').click()

#     # connect
#     #driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[4]/section/div[2]/button').click()
    
#     # confirm connection
#     #driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    

# except Exception as e: 
#     print(e)
#     driver.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Path to your webdriver executable (e.g., chromedriver)
# webdriver_path = r"C:\Users\asus\Downloads\chromedriver_win32"
# Download ChromeDriver and place it in the working directory
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")

# Enter email and password 
driver.find_element(By.ID, "username").send_keys("alhydrym7@gmail.com")
driver.find_element(By.ID, "password").send_keys("774390003Mm")

# Click sign in button 
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(3)

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
sleep(10)

driver.find_element(By.ID, "ember36").click()
sleep(5)
driver.find_element(By.ID,"ember84").click()
sleep(10)
# Go to your network page

# Find and click on the "Manage" button to see the list of people you follow
#driver.find_element(By.CLASS_NAME, 'ember-view mn-invitations-preview__manage-all artdeco-button artdeco-button--tertiary artdeco-button--muted artdeco-button--2')

#
# Wait for the list to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'self-focused ember-view')))

# # Get the list of connections and iterate over them
# connections = driver.find_elements(By.CLASS_NAME, 'mn-connection-card')
# for connection in connections:
#     # Check if the connection is not following you
#     if 'Follows you' not in connection.text:
#         # Click on the 'More' button to reveal the unfollow option
#         more_button = connection.find_element(By.CLASS_NAME, 'mn-connection-card__dropdown-trigger')
#         more_button.click()
        
#         # Click on the 'Remove connection' option to unfollow
#         remove_button = driver.find_element(By.CLASS_NAME, 'mn-connection-card__dropdown-option')
#         remove_button.click()

#         # Confirm the unfollow action in the modal
#         confirm_button = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
#         confirm_button.click()

# Close the browser

