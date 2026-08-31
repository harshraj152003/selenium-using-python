from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Locate the search input box using Name attribute
element = driver.find_element(By.NAME, "q")

# Basic Interactions
element.clear()  # Clear existing text
element.send_keys("Selenium Python")  # Type text into input field
element.send_keys(Keys.ENTER)  # Press Enter key

# Reading Element Properties
# Wait up to 10 seconds for the element to appear
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3")))
print("Header Text:", first_result.text)  # Extract visible text
print("Tag Name:", first_result.tag_name)
print("Attribute Value:", first_result.get_attribute("class"))

# Checking State
print("Is Displayed?:", first_result.is_displayed())  # Returns True/False
print("Is Enabled?:", first_result.is_enabled())  # Returns True/False

driver.quit()