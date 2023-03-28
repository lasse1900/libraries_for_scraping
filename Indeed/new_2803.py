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




# username.send_keys("lauri.kyttala@gmail.com")
# password=browser.find_element(By.XPATH,value="session_password")
# # password=browser.find_element(By.CSS_SELECTOR,'/html/body/main/section[1]/div/div/form[1]/div[1]/div[2]/div/div/input')
# username.send_keys("TAmmiholma8")

# login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
# login_button=browser.find_element(By.XPATH,value="//*[@id='main-content']/section[1]/div/div/form[1]/div[2]/button")
# login_button.click()

# browser.get("https://www.linkedin.com/")