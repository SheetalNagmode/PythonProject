#  Test Case
#
# 1) Open Web Browser (Chrome/firefox/Edge)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual Title)
# 7) Verify title of the page: OrangeHRM   (Expected)
# 8) Close browser

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service= Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)    # wait max 10 sec for elements

driver.get("https://opensource-demo.orangehrmlive.com/")

# time.sleep(1)  # Keeps browser open for 10 seconds

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

time.sleep(2)

driver.close()



