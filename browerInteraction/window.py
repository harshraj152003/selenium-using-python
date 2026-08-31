from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window() # Maximize browser window
driver.get("https://www.google.com") # Navigate to Google

print("Current url:",driver.current_url)  # https://www.google.com/
print("Title:",driver.title) # Google

driver.get("https://www.bing.com")

driver.back() # Go back to 
time.sleep(2)

driver.forward() # Go forward to Bing
print("Title:",driver.title)
time.sleep(2)

driver.refresh() # reload the current page
time.sleep(2)

driver.close()  # Closes current tab
driver.quit()  # Closes all tabs & terminates browser process