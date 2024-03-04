from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

load_dotenv()

PATH = Service("C:\Program Files (x86)\Selenium\msedgedriver.exe")
driver = webdriver.Edge(service=PATH)

driver.get("https://www.linkedin.com/")

# Maximize the window
driver.maximize_window()

# Sign into my account
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
email.send_keys(os.getenv("INDEED_EMAIL") + Keys.ENTER)

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_password")))
password.send_keys(os.getenv("LINKEDIN_PASSWORD") + Keys.ENTER)

time.sleep(10)

# Wait for the Jobs tab to be clickable and click it
jobs_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Jobs")))
jobs_tab.click()

# Search Parameters
search_keyword = "Data Analyst"
search_location = "Toronto, ON"

# Find the "Keywords" input element and enter search keyword
input_job = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
input_job.clear()
input_job.send_keys(search_keyword)


input_location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='City, state, or zip code']")))
input_location.clear()
input_location.send_keys(search_location + Keys.ENTER)

time.sleep(10)


#Apply filters to the search results
easy_apply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Easy Apply filter.']")))
easy_apply.click()

time.sleep(5)











# Additional actions can be performed here, such as scraping the job listings

driver.quit()
