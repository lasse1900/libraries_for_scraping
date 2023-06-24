# https://www.youtube.com/watch?v=X9OXAV7SGmM

# url = 'https://fi.linkedin.com/jobs/search?keywords=%s'

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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url1='https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

driver.get(url1)
driver.implicitly_wait(60)