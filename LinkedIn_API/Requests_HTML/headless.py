from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import timeit

#Timer starts 
start = timeit.default_timer()
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("headless")
#chrome_options.add_argument("--window-size=1920x1080")

# go to google
driver = webdriver. Chrome(chrome_options=chrome_options, executable_path="C:\\bin\\chromedriver.exe")
driver.get("https://www.indeed.com")
driver.maximize_window()

#Sending selenium in search field 
driver.find_element_by_xpath("//*[@id='text-input-what']").send_keys("Selenium")

#Timer Stops
stop = timeit.default_timer()
#Prints the Start and End Time to Console
print('Time: ', stop - start)