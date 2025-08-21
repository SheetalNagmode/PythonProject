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
from selenium.webdriver.chrome.service import Service

service= Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)  # Keeps browser open for 5 seconds



