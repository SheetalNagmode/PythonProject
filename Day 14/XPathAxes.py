import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self

# text_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Max Estates']/self::a").text
# print(text_msg)

# parent

text_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Max Estates']/parent::td").text
print(text_msg)


