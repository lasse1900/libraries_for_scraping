
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = True
options.add_argument('window-size=1920*1080')

# define the website to scrape and path where the chromediver is located
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'C:/bin/chromedriver.exe'
service = Service(executable_path=path)  # selenium 4
driver = webdriver.Chrome(service=service)  # define 'driver' variable
# open Google Chrome with chromedriver
driver.get(website)
# driver.maximize_window()