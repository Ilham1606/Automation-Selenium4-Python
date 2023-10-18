from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import codecs
import time


# setups WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/v1/")

file_path = "myenv/data_test.csv"

# Open CSV file, read and delimiter (';')
with codecs.open(file_path, "r", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row)

        # Login elements
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(row[0])
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(row[1])
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # statement & Assertions
        if row[2] == "passed":
            inventory_list = driver.find_element(
                By.XPATH, "//div[@class='inventory_list']"
            )
            assert inventory_list.is_displayed()
            print("Inventory List displayed")
        else:
            error_message = driver.find_element(
                By.XPATH, '//button[@class="error-button"]'
            )
            assert error_message.is_displayed()
            print("Failed, Invalid Credentials")
            time.sleep(1)

        # Back to login page
        driver.get("https://www.saucedemo.com/v1/")

# Close WebDriver
driver.quit()
