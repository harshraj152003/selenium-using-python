from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=38SFCGQUD9B7Q&sprefix=laptop%2Caps%2C257&ref=nb_sb_noss_2")
elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"Number of items: {len(elems)}")
print(elems)
for elem in elems:
    print(elem.text)

driver.close()