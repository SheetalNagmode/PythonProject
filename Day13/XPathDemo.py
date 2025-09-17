import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Absolute XPath

#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Apple MacBook Pro")
#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# time.sleep(2)

# Relative XPath
# driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Apple MacBook Pro")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# time.sleep(1)

# or / and

#driver.find_element(By.XPATH,"//input[@id='small_searchterms'or @name='q']").send_keys("Apple MacBook Pro")
#driver.find_element(By.XPATH,"//input[@class='search-box-text ui-autocomplete-input'and @name='q']").click()

#time.sleep(4)

# contains()  & start-with()

#driver.find_element(By.XPATH,"//input[contains(@id,'small')]").send_keys("Apple MacBook Pro")
#driver.find_element(By.XPATH,"//button[starts-with(@type,'sub')]").click()

#time.sleep(2)

# text()
driver.find_element(By.XPATH, "//a[text()='Register']").click()

time.sleep(2)