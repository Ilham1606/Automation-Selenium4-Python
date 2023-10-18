from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\chromedriver-win32\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.saucedemo.com/v1/')

