# This is a python script to perform web-scraping. 
# Tasks performed are:
# 1. Scrapes data from two given web pages (collects first and last names)
# 2. Creates 20 names combinations, fake email address, password
# 3. Writes the above data into a .txt file
#
# Constraint: Use headless chrome to scrape data from webpages
#
# Necessary conditions for the script to compile:
# 1. chromedriver must be installed in the current working directory
# 2. Tools need to be installed: selenium
# Output:  persons20.txt in the current working directory
# Author: Saveri Pal
# Last edit: April 23, 2019
# ------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# set chrome to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# gets chromedriver from current working directory
chrome_driver = os.getcwd() +"/chromedriver"

# launches chrome
driver = webdriver.Chrome(chrome_options= chrome_options, executable_path=chrome_driver)

# scraping for 10 last names
driver.get('https://www.rong-chang.com/namesdict/100_last_names.htm')
# list to store last names
lnames = []
for i in range(1,11):
        x = driver.find_element_by_xpath("//table/tbody/tr/td[1]/b[%d]/a"%i)
        y = x.text
        lnames.append(y)

# scraping for 2 first names
driver.get('https://www.mother.ly/news/the-most-popular-baby-names-of-2017')
# list to store first names
fnames = []
name1 = driver.find_element_by_xpath("//table/tbody/tr[2]/td[2]")
name2 = driver.find_element_by_xpath("//table/tbody/tr[2]/td[3]")
fnames.append(name1.text)
fnames.append(name2.text)

#print(lnames)
#print(fnames)

# create a new output file
f = open("persons20.txt","w")

# Adds 20 names and details to file. Each line consists of: firstName lastName password email
for j in range(1,3):
	for k in range(1,11):
		email = fnames[j-1] + lnames[k-1] + "@fakemail.com"
		password = fnames[j-1][0]+"4798"+lnames[k-1]+"$%!"
		person = fnames[j-1]+" "+lnames[k-1]+" "+password+" " +email
		f.write(person)
		f.write("\n")

f.close()






