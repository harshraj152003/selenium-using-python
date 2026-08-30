# Selenium Web Automation & Scraping Notes

A structured learning repository for Python-based web automation and data scraping using Selenium. This repository tracks fundamental concepts, locator strategies, DOM extraction, and multi-page data scraping on Amazon India.

---

# Comprehensive Guide to Selenium: Deep Dive, Architecture & Evolution

This guide provides an in-depth exploration of Selenium—covering its history, underlying architecture, browser integration mechanics, and why it remains an industry standard for web automation and testing.

---

## 📜 History & Evolution of Selenium

### 1. The Origins (2004)

- **Creation:** Selenium was created in 2004 by **Jason Huggins** while working at ThoughtWorks.
- **The Problem:** He was testing an internal Python application and realized that manually executing repetitive test cases across browser UI builds was inefficient and error-prone.
- **The Initial Fix:** He wrote a JavaScript program named **JavaScriptTestRunner** to automatically control browser actions, inspect DOM elements, and validate page states.

### 2. The Birth of Selenium Core & Remote Control (RC)

- **Rename to Selenium:** The program was open-sourced and renamed **Selenium** (as a playful joke contrasting it with a competing testing framework of the era named _Mercury_).
- **Same-Origin Policy Limitations:** Because JavaScriptTestRunner ran purely inside the browser sandbox, browsers blocked it from interacting with domains other than the one hosting the script due to the **Same-Origin Policy (SOP)**.
- **Selenium RC (Selenium 1):** Created by **Paul Hammant**, Selenium RC introduced a HTTP proxy server. The server tricked the browser into believing that Selenium Core and the web application under test belonged to the exact same domain, bypassing SOP restrictions.

### 3. The WebDriver Revolution (2007–2011)

- **The WebDriver Project:** In 2007, **Simon Stewart** created WebDriver at Google. Unlike Selenium RC, WebDriver bypassed the JavaScript sandbox entirely by controlling the browser natively at the OS level using native browser drivers.
- **Selenium 2 (2011):** Selenium RC and WebDriver merged in 2011 to form **Selenium 2.0**, establishing WebDriver as the primary engine for web automation.

### 4. W3C Standardization & Modern Era (Selenium 3 & 4)

- **Selenium 3 (2016):** Fully deprecated Selenium RC, enforcing native driver communication via custom JSON Wire Protocol contracts.
- **W3C Standard (2018):** WebDriver officially became an official **W3C Recommendation**, standardizing browser automation across Chrome, Firefox, Safari, and Edge.
- **Selenium 4 (2021–Present):** Adopted 100% W3C standard compliance, replaced the old JSON Wire Protocol with direct W3C HTTP communication, and introduced native Chrome DevTools Protocol (CDP) integration.

---

## 🏗️ How Selenium Works (Architecture & Protocols)

Selenium operates using a 4-tier client-server architectural model:

````text
+-----------------------+      W3C HTTP      +------------------+      Native OS      +------------------+
|  Client Code          |  ================> |  Browser Driver  |  ================>  |  Target Browser  |
| (Python/Selenium SDK) | <================  | (e.g.chromedriver)| <================  | (Chrome/Firefox) |
+-----------------------+     JSON / HTTP    +------------------+      Commands       +------------------+
````

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
```

## 📋 Prerequisites & Requirements

Before running the scripts in this repository, ensure your environment meets the following requirements:

* **Python**: Version 3.8 or higher installed on your machine.
* **Google Chrome**: Latest version of the Chrome browser installed.
* **Operating System**: macOS, Linux, or Windows.

> **Note on Drivers**: Selenium 4 handles ChromeDriver downloads and configuration automatically via its built-in `selenium-manager`. You do **not** need to manually download or configure path variables for `chromedriver`.

---

## ⚙️ Setup & Installation

Follow these steps to set up the project locally:

### Clone the Repository
```bash
git clone [https://github.com/harshraj152003/selenium-using-python.git](https://github.com/harshraj152003/selenium-using-python.git)
cd selenium-using-python
```
