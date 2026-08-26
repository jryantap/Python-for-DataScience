### script that will search through a ServiceNow page for specific keywords
### for "potential outage"
### 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# set keywords here for now, hard coded.
KEYWORDS = ["epic reports"]

### Plan:
### get the website page
### search all visible table rows on that current page

# get the website page 
driver = webdriver.Chrome()
driver.get("http://example.com") #should be the direct link for the ServiceNow page or any page appropriate for the seach

# must login to the dashboard with user's credentials then get prompted 
# this is the prompt 
input ("Login to the dashboard and press Enter once done." )

# create a list to store matches
matches = []

#find the elements here in the page
rows = driver.find_elements(By.XPATH, "//tr") 

# loop through the rows and check for keywords
# (still testing, not sure if this will work, but it should)

for row in rows:  #go through each row that selenium found
    row_text = row.text.strip()   # remove extra spaces and newlines

    # check if any of the keywords are in the row text
    if not row_text:  # skip empty rows
        continue # this will skip the rest of the loop and go to the next row

    # make all of them lower case if found
    row_text_lower = row_text.lower()

    # store them 
    found_keywords = []

    for keyword in KEYWORDS:  # check every keyword in the list

        if keyword.lower() in row_text_lower:  # check if the keyword is in the row text
            found_keywords.append(keyword)  # add the found keyword to the list

# when keywords are found, store the row text and the keywords found in the matches list

    if found_keywords:  # if any keywords were found
        matches.append((row_text, row_text))  # store the row text and the found keywords

        ####plan:  possibly highlight the row in the page, but not sure how to do that yet.  Will have to look into it.  Maybe use javascript to change the background color of the row.   
        

        driver.execute_script(""""
                              arguments[0].style.outline = '3px solid yellow';
                              arguments[0].style.backgroundColor = 'yellow';
                              """, row)

#print the matches found
print (f"\nFound {len(matches)} maching rows:\n") # I think this is right, have to double check the notation.

## maybe use non f-string.
## print("\nFound " + str(len(matches)) + "matching rows: \n")

#Results will be printed in the console, but could also be written to a file if needed.
### untest at the moment. 


