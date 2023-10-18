from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import codecs
import time

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# setup
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

# actions & elements
user_name = driver.find_element(By.XPATH, "//input[@name='username']").send_keys(
    "Admin"
)
password = driver.find_element(By.XPATH, "//input[@type='password']").send_keys(
    "admin123"
)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

expected_text = driver.find_element(By.TAG_NAME, "h6").text
assert expected_text, f"Expected '{expected_text}'"
print(f"Expected Text is [", expected_text,"]")

#driver.find_element(By.XPATH, "//span[text()='Admin']").click()

# for i in range(2):
#     delete_record_elements = f"//div[@class='oxd-table-cell-actions']//i[@class='oxd-icon bi-trash-{i+1}']"
#     driver.find_element(By.XPATH, delete_record_elements).click()

time.sleep(3)
driver.quit()
