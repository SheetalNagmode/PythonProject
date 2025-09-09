import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service= serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

sliders= driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))

links= driver.find_elements(By.TAG_NAME, 'a')
print(len(links))