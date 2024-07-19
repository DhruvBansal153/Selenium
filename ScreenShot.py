from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.get("http://www.google.com.")
search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("House of Dragon")
search.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div[1]/div/div/span/a').click()
driver.save_screenshot("C:/Users/dhruv/OneDrive/Desktop/Selenium/Selenium/screenshots/first.png")
time.sleep(10)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(6)