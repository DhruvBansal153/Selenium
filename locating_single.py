from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "phone"
driver.get(f"https://www.amazon.in/s?k={query}&crid=25E96DT0LIJB0&sprefix=lapto%2Caps%2C284&ref=nb_sb_noss_2")
elem=driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(5)
driver.close()