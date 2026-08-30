from selenium import webdriver

driver = webdriver.Chrome()
driver.get(f"https://www.amazon.in/s?k=laptop&crid=38SFCGQUD9B7Q&sprefix=laptop%2Caps%2C257&ref=nb_sb_noss_2")

driver.close()