# This is a python script to fill an online form - Google accounts creation page
# Tasks performed are:
# 1. Uses chrome to visit Google accounts creation page
# 2. Reads a file named 'persons20.txt' and takes the first line to populate the fields in the page
# 3. Fields populated are - first name, last name, username, password, confirm password, then hits 'Next' button
# 4. Modification: a simple for-loop can be added to the script to repeat step 1-3 for all 20 generated names
#
# Necessary conditions for the script to compile:
# 1. chromedriver must be installed in the current working directory
# 2. This script must be located in the current working directory of 'persons20.txt' or a similar text file
# 3. Tools needs to be installed: selenium
# 
# Output: chrome browser window at google accounts creation page with automated field population
# Author: Saveri Pal
# Last edit: April 23, 2019
# -------------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# gets chromedriver from current working directory
chrome_driver = os.getcwd() +"/chromedriver"

# launches chrome 
driver = webdriver.Chrome(executable_path=chrome_driver)

# GOOGLE ACCOUNT CREATION PAGE

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
driver.implicitly_wait(10)

firstN = driver.find_element_by_name('firstName')
lastN = driver.find_element_by_name('lastName')
userN = driver.find_element_by_name('Username')
passwrd = driver.find_element_by_name('Passwd')
confirmpasswrd = driver.find_element_by_name('ConfirmPasswd')
clicknext = driver.find_element_by_id('accountDetailsNext')

# Reads the 1st line of  persons20.txt and populates form 

f = open("persons20.txt","r")
line = f.readline()
#print(line)
word = line.split(" ")
#print(word[3])

firstN.send_keys(word[0])
lastN.send_keys(word[1])
x = word[0]+"tenheads"
userN.send_keys(x)
passwrd.send_keys(word[2])
confirmpasswrd.send_keys(word[2])
clicknext.click()

# ----------------------------------------------------------------------------
# FACEBOOK LOGIN PAGE
#driver.get('https://facebook.com')
#driver.implicitly_wait(10)

#email = driver.find_element_by_css_selector('input[type=email]')
#password = driver.find_element_by_css_selector('input[type=password]')
#login = driver.find_element_by_css_selector('input[value="Log In"]')

#x = "tommy@rocketmail.com"
#email.send_keys(x)
#password.send_keys('hilfiger')
#login.click()
# ----------------------------------------------------------------------------------

