from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/jibril/Documents/Advanced/chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
