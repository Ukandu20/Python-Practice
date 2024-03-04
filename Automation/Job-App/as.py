#Sign into my account
#Click the sign in button
sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in.click()

#Wait for the email input to be located on the page
email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1"))
    )
#Input your email address   and password
email.send_keys(os.getenv("INDEED_EMAIL") + Keys.ENTER)
time.sleep(20000)

#Verify you are human captcha

#Click the verify button
verify = driver.find_element(By.ID, "captcha-internal-button")
verify.click()



password = driver.find_element(By.ID, "gsuite-login-google-button")
time.sleep(2) #Give the page time to load
password.click()
time.sleep(200000)



#Locate the search bar element by its ID
search_bar = driver.find_element(By.CLASS_NAME, "jobs-search-box-keyword-id-ember522")
search_bar.clear()
search_bar.send_keys("Python Developer" + Keys.ENTER)
time.sleep(20)

#Locate the location bar element by its ID
location_bar = driver.find_element(By.CLASS_NAME, "jobs-search-box-location-id-ember522")
location_bar.click()
location_bar.send_keys("Toronto, ON" + Keys.ENTER)
time.sleep(20)





#Search for a job using Python Developer as the search keyword
search_bar = driver.find_element(By.ID, "jobs-search-box__container jobs-search-box jobs-home-redesign__search-boxes ")
search_bar.clear()
search_bar.send_keys("Python Developer" + Keys.ENTER)

#Get the total number of results
total_results = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.ID, "searchCountPages"))
     )[0].text
num_pages = int(''.join([i for i in total_results if i.isdigit()]))

#Print out how many pages there are
print(f"\nThere are {num_pages} pages of results for Python Developer jobs in Toronto, ON")

#Go through each page of results and apply to each job that is not full time
for i in range(1, num_pages + 1):       
    #Get all the job listings on the page
    job_listings = driver.find_elements(By.PARTIAL_LINK_TEXT, "Python Developer")
    
    #Loop through the job listings and apply for each one
    for job in job_listings:
        #Click the job listing
        job.click()
        time.sleep(5)

        #Wait for the 'Apply now button' to be located
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Apply Now"))
        )
        
        #Click the 'Apply Now' button
        apply_now = driver.find_element(By.PARTIAL_LINK_TEXT, "Apply Now")
        apply_now.click()
        time.sleep(5)

        #Go back to the job listings page
        driver.back()
        time.sleep(5)
        job_listings = driver.find_elements(By.PARTIAL_LINK_TEXT, "Python Developer")

    #Go to the next page of results
    next_page = driver.find_element(By.PARTIAL_LINK_TEXT, str(i + 1))
    next_page.click()
    time.sleep(5)   

#Search for a job using Data Analyst as the search keyword      

#Click the 'My Jobs' link       
my_jobs = driver.find_element(By.PARTIAL_LINK_TEXT, "My Jobs")  
my_jobs.click()     
time.sleep(2)



# wait for the search input element to be located
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text-input-what"))
    )

#Search Parameters
search_keyword = "Data Analyst"
search_location = "Toronto, ON"

# find the "SEARCH" input element by its class name and type in it
input_job = driver.find_element(By.ID, "text-input-what")
input_job.clear()
input_job.send_keys(search_keyword + Keys.ENTER)

# wait for the search input element to be located
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text-input-where"))
    )

#find the city input element by its class name and type in it
city_select = driver.find_element(By.ID, "text-input-where")
city_select.clear()
city_select.send_keys(search_location + Keys.ENTER)


# wait for the search input element to be located
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, search_keyword))
    )

#find all the job listings on the page
job_listings = driver.find_elements(By.PARTIAL_LINK_TEXT, search_keyword)

#loop through the job listings and apply for each one
for job in job_listings:

    #click the job listing
    job.click()
    time.sleep(5)

    #Wait for the 'Apply now button' to be located
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Apply Now"))
    )
    
    #Click the 'Apply Now' button
    apply_now = driver.find_element(By.PARTIAL_LINK_TEXT, "Apply Now")
    apply_now.click()
    time.sleep(5)

    
    driver.back()
    time.sleep(5)
    job_listings = driver.find_elements(By.PARTIAL_LINK_TEXT, search_keyword)