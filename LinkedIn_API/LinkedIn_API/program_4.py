#Import Packages
from selenium import webdriver
import time
import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python?noredirect=1&lq=1
ser = Service(r'C:\\bin\\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")

# GitHub-repo & Youtube-video links below
# https://github.com/vyasadi/LinkedIn-Job-Scraping/blob/main/linkedinjobspython.ipynb
# https://www.youtube.com/watch?v=3vwKBO9YkBI&t=24s

#Use this Url and change city or role accordingly

url1='https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
driver.get(url1)

#Find number of job listings

# driver.find_elements_by_class_name('results-context-header__job-count')[0].text
# driver.find_element(by=By.CLASS_NAME, value='results-context-header__job-count')[0].text
