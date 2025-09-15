import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service= serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# Tag & Id
# tagname#valueofID

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

# tag and class:
# tagname.valueofClass  input.inputtext _55r1 _6luy
# when there is a space after text you can omit that part and just put inputext

# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag and attribute
# tagname[attribute=value]     input[data-testid=royal-email]

driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys("abc@gmail.com")

# time.sleep(2)

# tag, class & attribute
# tagname.valueofClass[attribute=value]     input.inputtext[data-testid=royal_pass]

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("xyz")
