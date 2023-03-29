#Import Packages
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

cookies_accept_xpath = "//*[@id='onetrust-accept-btn-handler']"
input_field = "//*[@id='text-input-what']"
search_button = "//*[@id='jobsearch']/button"
browser = webdriver.Chrome()
browser.get("https://fi.indeed.com/")
username = browser.find_element(By.XPATH,value=cookies_accept_xpath)
search_field = browser.find_element(by=By.XPATH, value=input_field)
search_field.send_keys("embedded")
search_button = browser.find_element(By.XPATH,value=search_button)
search_button.click()
browser.implicitly_wait(2)
browser.get_screenshot_as_file('indeed.png') 
