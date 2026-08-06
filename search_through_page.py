# script that will search through a ServiceNow page for specific keywords

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# set keywords here for now, hard coded.
KEYWORDS = ["MyChart", "Anesthesia", "missing CI", "Cisco AnyConnect"]

# Plan:
# get the website page
# search all visible table rows on that current page

# get the website page 
driver = webdriver.Chrome()
driver.get("http://example.com") #should be the direct link for the ServiceNow page

# must login to the dashboard with user's credentials then get prompted 
# this is the prompt 
input ("Login to the dashboard and press Enter once done." )

# create a list to store matches
matches = []

#find the elements here in the page
rows = driver.find_elements(By.XPATH, "//tr") 

# loop through the rows and check for keywords

 