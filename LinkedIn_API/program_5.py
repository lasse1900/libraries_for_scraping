#Import Packages
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com")
username=browser.find_element(By.ID,value="session_key")
# username=browser.find_element(By.CSS_SELECTOR,'/html/body/main/section[1]/div/div/form[1]/div[1]/div[1]/div/div/input')
username.send_keys("lauri.kyttala@gmail.com")
password=browser.find_element(By.XPATH,value="session_password")
# password=browser.find_element(By.CSS_SELECTOR,'/html/body/main/section[1]/div/div/form[1]/div[1]/div[2]/div/div/input')
username.send_keys("TAmmiholma8")

# login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
# login_button=browser.find_element(By.XPATH,value="//*[@id='main-content']/section[1]/div/div/form[1]/div[2]/button")
# login_button.click()

# browser.get("https://www.linkedin.com/")