# Selenium Basics & Web Scraping Notes

A clean reference guide covering browser automation, element locator strategies, HTML extraction, and multi-page web scraping using Python and Selenium.

---

## 📁 Project Structure

- **`data/`**: Directory used to store scraped raw HTML files for offline processing.
- **`boiler.py`**: Initial browser setup, basic navigation, reading browser state, and teardown logic using try/finally blocks.
- **`locating_multiple.py`**: Locating collections of DOM nodes matching shared class names and extracting text from multiple elements.
- **`locating_single.py`**: Finding a single targeted element, printing its text content, and inspecting raw HTML attributes.
- **`project.py`**: Paginated multi-page web scraping, extracting raw element markup, and saving dynamic dumps to disk.

---

## 🔑 Imports & Core Functions Reference

### 1. `from selenium import webdriver`

- **What it is:** The primary module in Selenium used to launch and control web browser instances.
- **Why it is used:** It provides the driver object (`webdriver.Chrome()`) that controls browser execution and user interaction.

---

### 2. `from selenium.webdriver.common.by import By`

- **What it is:** A locator class used to specify how DOM elements are targeted within a web page.
- **Why it is used:** It provides standard strategy constants such as `By.CLASS_NAME`, `By.ID`, `By.XPATH`, `By.CSS_SELECTOR`, and `By.TAG_NAME`.

---

### 3. `import time`

- **What it is:** Python's built-in time handling module.
- **Why it is used:** Used to pause script execution (`time.sleep()`) to wait for pages or elements to load.

---

## 🛠️ Method & Attribute Breakdown

### Browser Lifecycle & Navigation

- **`webdriver.Chrome()`**: Initializes a new Chrome browser driver instance.
- **`driver.get(url)`**: Directs the automated browser to open and navigate to the specified URL.
- **`driver.title`**: Fetches the title of the currently active web page.
- **`driver.close()`**: Closes the currently active browser window or tab.
- **`driver.quit()`**: Completely terminates the driver session and closes all open windows, ensuring clean resource teardown.

---

### Element Finding Strategies

- **`driver.find_element(By.CLASS_NAME, "...")`**: Searches the DOM and returns the **first matching single element**. Raises an exception if no element matches.
  - **Where used:** `locating_single.py` (used to target `"puisg-row"`)
- **`driver.find_elements(By.CLASS_NAME, "...")`**: Searches the DOM and returns a **list of all matching elements**. Returns an empty list if none are found.
  - **Where used:** `locating_multiple.py`, `project.py` (used to target `"puis-card-container"`)

### Data Extraction & File Handling

- **`elem.text`**: Extracts visible text content contained inside a Web Element node.
  - **Where used:** `locating_multiple.py`, `locating_single.py`
- **`elem.get_attribute("outerHTML")`**: Retrieves the full raw HTML string markup of the targeted element node (including its outer tag).
  - **Where used:** `locating_single.py`, `project.py`
- **`open(filepath, "w")`**: Python standard file operator used to write extracted HTML strings directly into storage files.
  - **Where used:** `project.py` (saves HTML files sequentially as `data/laptop_X.html`)

---

## 📌 File-by-File Summary & Workflow

### 1. `boiler.py`

- **Objective:** Establish browser driver initialization and safe shutdown patterns.
- **Key Tasks:** Launches Chrome driver, navigates to Google, reads `driver.title`, sleeps briefly, and guarantees shutdown using `try...finally` with `driver.quit()`.

### 2. `locating_multiple.py`

- **Objective:** Extract data from multiple elements across a page.
- **Key Tasks:** Navigates to an Amazon search query, retrieves all matching item cards via `driver.find_elements()`, prints the element count, and iterates over each element to print visible `.text`.

### 3. `locating_single.py`

- **Objective:** Target specific single elements and extract raw markup.
- **Key Tasks:** Navigates to Amazon, locates a single row container via `driver.find_element()`, prints visible `.text`, and retrieves raw DOM structure using `get_attribute("outerHTML")`.

### 4. `project.py`

- **Objective:** Implement pagination loops and disk persistence.
- **Key Tasks:** Iterates over Amazon search result pages (1 to 19), locates product cards per page, extracts their `outerHTML`, and saves each product card into individual files inside the `data/` directory.

---

## 💡 Best Practice Notes

1. **Directory Setup:** Ensure the `data/` directory is created before running multi-page scrapers like `project.py`.
2. **Session Cleanup:** Prefer `driver.quit()` over `driver.close()` to ensure driver background processes are completely released.
