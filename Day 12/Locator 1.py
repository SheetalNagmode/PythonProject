
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service= serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()    # maximize the browser window

# first two locators to find an element on the webpage
# ID and NAME example:

#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# Linktext & Partial Linktext

driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By. PARTIAL_LINK_TEXT, "Reg").click()

time.sleep(2)

# driver.close()  # close only one browser
# driver.quit()   # close all the browsers