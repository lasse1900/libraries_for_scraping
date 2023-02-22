# https://www.youtube.com/watch?v=NsSqHkFkiAs&list=PL_8jNcohs27U7hhyYsd-fxtdtxhmj204F
from selenium import webdriver
import pandas as ps

path = 'c:/bin/chromedriver'

# set path for the driver
browser = webdriver.Chrome(executable_path=path)

url = 'http://www.scrapethissite.com/pages/simple/'
# url = "https://scrapethissite.com/pages/simple/"
# open the page url in chrome
browser.get(url)

# Sraping the data - get country names
# country_list = browser.find_elements("//h3[@class='country-name']")

# # parse the data
# countries = []
# for country in country_list:
#     # get the text data
#     temp = country.text
#     countries.append(temp)

# countries

# population_list = browser.find_elements("//span[@class='country-population']")
browser.close
