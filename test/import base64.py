# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set the URL for the Tinder login page
login_url = 'https://tinder.com/app/login'

# Set the username and password for the bot account
username = 'bot_username'
password = 'bot_password'

# Set the message to send to matches
message = 'Hello, are you enjoying the app?'

# Create a web driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find the username and password inputs
username_input = driver.find_element_by_name('email')
password_input = driver.find_element_by_name('password')

# Enter the username and password
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.ENTER)

# Wait for the login process to complete
# (You may need to add additional code here to handle the login process)

# Find the "like" button
like_button = driver.find_element_by_css_selector('.button-text--like')

# Click the "like" button
like_button.click()

# Wait for the match notification
sleep(1)

# Find the match notification
match_notification = driver.find_element_by_css_selector('.match-header')

# Click the match notification
match_notification.click()

# Wait for the chat window to load
sleep(1)

# Find the chat input
chat_input = driver.find_element_by_css_selector('.message-input')

# Enter the message
chat_input.send_keys(message)

# Send the message
chat_input.send_keys(Keys.ENTER)
