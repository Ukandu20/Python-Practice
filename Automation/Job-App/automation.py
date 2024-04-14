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
# Maximize the window
driver.maximize_window()


driver.get("https://www.linkedin.com/")



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


#Loop Through every listing and apply for each of the jobs. Add each Applied job to a database list to keep track of applied jobs.
#Loop through the job listings
job_listings = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='job-card-container relative job-card-list job-card-container--clickable job-card-list--underline-title-on-hover jobs-search-results-list__list-item--active-v2 jobs-search-two-pane__job-card-container--viewport-tracking-0']")))


for job in job_listings:
    job_listings.click()
    time.sleep(3)

    #Check if the job has already been applied to
    try:
        applied_message = driver.find_element(By.XPATH, "//span[@class='artdeco-inline-feedback__message']")
        print("Already applied to this job")
        continue  # Skip to the next job listing
    except:
        pass

    # Apply for the job
    try:
        easy_apply_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']")))
        easy_apply_button.click()
        time.sleep(3)
    
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")))
        next_button.click()
        time.sleep(20)

    except Exception as e:
        print(f"Failed to apply for the job: {e}")
    
    # Go back to the search results
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)





# Additional actions can be performed here, such as scraping the job listings

driver.quit()
