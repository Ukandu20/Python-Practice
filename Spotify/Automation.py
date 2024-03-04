#Import Selenium
from selenium import webdriver

PATH = "C:\Program Files (x86)\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")


