from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=38SFCGQUD9B7Q&sprefix=laptop%2Caps%2C257&ref=nb_sb_noss_2")
elem = driver.find_element(By.CLASS_NAME,"puisg-row")
print(elem.text)
print(elem.get_attribute("outerHTML"))
time.sleep(5)

driver.close()