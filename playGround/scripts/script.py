import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    """Initializes and configures the Selenium WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def task1_open_playground(driver):
    """Open the main HTML practice playground page."""
    driver.get("file:///Users/admin/selenium-practice/playGround/html/index.html")


def task2_redirect_to_target(driver):
    """Click on the redirect link to navigate to the target hover page."""
    target_link = driver.find_element(By.ID, "target-link")
    target_link.click()


def task3_hover_and_click_data(driver):
    """Automate the Hover Div in the new page, click Data 1 once revealed, and accept the alert."""
    # Locate hover container
    hover_container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mouse-hover-container"))
    )

    # Perform mouse hover action
    actions = ActionChains(driver)
    actions.move_to_element(hover_container).perform()

    # Click 'Data 1' option inside the hover menu
    data_1_btn = driver.find_element(By.ID, "data-1-btn")
    data_1_btn.click()

    # Handle and accept the resulting alert
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"Alert Text Captured: {alert.text}")
    alert.accept()


def main():
    """Main function to execute all selenium tasks sequentially."""
    driver = setup_driver()

    try:
        print("Executing Task 1: Opening Playground...")
        task1_open_playground(driver)

        print("Executing Task 2: Redirecting to target page...")
        task2_redirect_to_target(driver)

        print("Executing Task 3: Hovering and clicking Data 1...")
        task3_hover_and_click_data(driver)

        print("All tasks completed successfully!")

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()