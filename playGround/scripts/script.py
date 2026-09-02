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


def task2_hover_workflow(driver):
    """Navigate to target-page.html, hover over menu, click Data 1, and handle alert."""
    target_link = driver.find_element(By.ID, "target-link")
    target_link.click()

    hover_container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mouse-hover-container"))
    )

    actions = ActionChains(driver)
    actions.move_to_element(hover_container).perform()

    data_1_btn = driver.find_element(By.ID, "data-1-btn")
    data_1_btn.click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"[Hover Task] Alert Text Captured: {alert.text}")
    alert.accept()


def task3_navigate_back_to_main(driver):
    """Navigate back to the index.html page."""
    script_dir = Path(__file__).parent
    index_path = (script_dir.parent / "html" / "index.html").resolve()
    driver.get(index_path.as_uri())


def task4_drag_and_drop(driver):
    """Navigate to drag-drop.html and drag the small div into the big target div."""
    drag_link = driver.find_element(By.ID, "drag-drop-link")
    drag_link.click()

    # Locate source (small div) and target (big div)
    source_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "draggable-source"))
    )
    target_element = driver.find_element(By.ID, "droppable-target")

    # Perform Drag and Drop using ActionChains
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    print("[Drag & Drop Task] Element successfully dragged and dropped!")


def main():
    """Main function to execute all task functions sequentially."""
    driver = setup_driver()

    try:
        print("Executing Task 1: Opening Main Playground...")
        task1_open_playground(driver)

        print("Executing Task 2: Hover and Alert Workflow...")
        task2_hover_workflow(driver)

        print("Executing Task 3: Returning to Main Page...")
        task3_navigate_back_to_main(driver)

        print("Executing Task 4: Drag and Drop Action...")
        task4_drag_and_drop(driver)

        print("All tasks completed successfully!")

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()