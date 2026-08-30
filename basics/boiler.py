import time
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    print("Page Title is:", driver.title)
    time.sleep(3)
finally:
    driver.quit()