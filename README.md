# Selenium Web Automation & Scraping Notes

A structured learning repository for Python-based web automation and data scraping using Selenium. This repository tracks fundamental concepts, locator strategies, DOM extraction, and multi-page data scraping on Amazon India.

---

## 📁 Repository Structure

```text
selenium-using-python/
├── basics/
│   ├── data/                   # Output folder storing scraped HTML dumps
│   ├── boiler.py               # Basic browser setup, title fetching, and teardown
│   ├── locating_single.py      # Extracting text & HTML attributes from a single DOM element
│   ├── locating_multiple.py    # Fetching collections of elements and extracting text
│   └── project.py              # Multi-page paginated scraping and writing HTML files to disk
└── .gitignore

## 📋 Prerequisites & Requirements

Before running the scripts in this repository, ensure your environment meets the following requirements:

* **Python**: Version 3.8 or higher installed on your machine.
* **Google Chrome**: Latest version of the Chrome browser installed.
* **Operating System**: macOS, Linux, or Windows.

> **Note on Drivers**: Selenium 4 handles ChromeDriver downloads and configuration automatically via its built-in `selenium-manager`. You do **not** need to manually download or configure path variables for `chromedriver`.

---

## ⚙️ Setup & Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/harshraj152003/selenium-using-python.git](https://github.com/harshraj152003/selenium-using-python.git)
cd selenium-using-python
