# 🚀 Pytest + Selenium + Allure Automation Framework (Dockerized)

This test automation framework is built with **Pytest + Selenium** and includes modern best practices
This repository contains a complete end-to-end automation testing framework using:

- ✅ Python + Pytest
- ✅ Selenium WebDriver
- ✅ Allure Reports
- ✅ Docker (Headless Chrome)
- ✅ Page Object Model (POM)
- ✅ Screenshot on failure (saved to disk + attached to report)
- ✅ Parallel Execution (via pytest-xdist)
- ✅ GitHub Actions CI integration
- ✅ Structured test categories
- ✅ Logging

---

## 🔧 Requirements (Local)

- Python 3.9+
- Google Chrome installed
- ChromeDriver matching your Chrome version
- Install dependencies:

```bash
pip install -r requirements.txt
```

---
### 🧱 Architecture Diagram

```
 tests/                    # Test scripts using PageFactory
 ├── test_login.py
 ├── test_cart_navigation.py
 └── ...
 
 pages/                   # Page Objects
 ├── base_page.py         # Common Selenium methods
 ├── login_page.py        # Login interactions
 ├── inventory_page.py    # Inventory & cart actions
 ├── page_factory.py      # Lazy-loaded singleton page instances
 
 utils/                   # Reusable utilities
 ├── data_loader.py       # JSON test data reader
 ├── driver_manager.py    # Singleton WebDriver
 └── logger.py            # Logging configuration
 
 conftest.py              # Pytest hooks, driver fixture, screenshot capture
 
 reports/                 # HTML and Allure reports, screenshots
 └── screenshots/
 
 Dockerfile.chrome        # Chrome+Python Docker setup
 pytest.ini               # Pytest config (markers, default args)
```

---

## ⚙️ Implemented Framework Features

| Feature                         | Description |
|----------------------------------|-------------|
| ✅ Page Object Model             | Each page has its own class with locators and actions. Improves modularity and reuse. |
| ✅ PageFactory Pattern           | Lazily loads page objects once per test and caches them. |
| ✅ Singleton WebDriver           | Ensures only one browser session per test. Set via `driver_manager.py`. |
| ✅ Allure Reporting              | Captures test steps, screenshots, severity levels, and links to failed steps. |
| ✅ Pytest HTML Reporting         | Generates a styled HTML report (`reports/report.html`) for local viewing. |
| ✅ Screenshot on Failure         | Automatically attaches screenshots to Allure + HTML report when a test fails. |
| ✅ Logging                       | Each test/module can log actions to `logs/`. Helps trace failures and reproduce bugs. |
| ✅ Dockerized Execution          | Easily run the entire suite with Docker and headless Chrome. |
| ✅ GitHub Actions CI             | Tests run automatically on every push. Results are attached as artifacts. |

---

## 🧪 Pytest Features Used

| Pytest Feature                  | How It's Used |
|----------------------------------|---------------|
| `@pytest.mark.parametrize`      | Data-driven testing from JSON (e.g. test_login). |
| `@pytest.mark.smoke` / `regression` | Categorizes test types; allows filtered runs like `pytest -m smoke`. |
| `@pytest.mark.flaky`            | Retries flaky tests (if rerunfailures plugin is enabled). |
| `@pytest.mark.skipif` / `xfail` | Conditional skipping for unsupported OS or known failures. |
| `pytest_runtest_makereport`     | Captures failures to attach screenshots and logs. |
| `pytest_html_results_table_row` | Customizes HTML report to show descriptions and status. |
| `--alluredir`, `--html`         | Report paths configured in pytest.ini and bash scripts. |
| `-n auto` (pytest-xdist)        | Executes tests in parallel across CPU cores. |

---

## 🚀 Running Locally

```bash
pytest
```

To generate both HTML and Allure reports:

```bash
pytest --html=reports/report.html --self-contained-html --alluredir=reports/allure-results
```

To view the Allure report:

```bash
# Install Allure CLI (if not already installed)
# Mac
brew install allure

# Windows
choco install allure

# Ubuntu/Linux (manual or from snap)
sudo apt install allure

# Serve the report
allure serve reports/allure-results
```

---

## 🐳 Running via Docker

### 🔨 Build the Docker Image

```bash
docker build -f Dockerfile.chrome -t pytest-allure .
```

### ▶️ Run Tests

```bash
docker run --rm -v $(pwd)/:/app/ pytest-allure
```

This will save the generated HTML + Allure reports there.

---

## 🔁 GitHub Actions (CI/CD)

GitHub Actions is configured in:

```
.github/workflows/selenium-tests.yml
```

This workflow:

- Runs on pushes and pull requests to `main`
- Builds the Docker image
- Runs tests in headless mode
- Uploads HTML and Allure reports as CI artifacts

---

## 📁 Project Structure

```
.
├── tests/                      # Test cases
├── conftest.py                # Fixtures and driver setup
├── requirements.txt           # Python dependencies
├── Dockerfile.chrome          # Dockerfile with Chrome/ChromeDriver setup
├── pytest.ini                 # Pytest config with default addopts
├── reports/                   # HTML and Allure reports
└── .github/workflows/         # CI workflows
```

---

## 🧪 Sample Test Run Output

```
tests/test_login.py::test_login[data0] PASSED
tests/test_login.py::test_login[data1] PASSED
tests/test_login.py::test_login[data2] PASSED

Generated HTML report: reports/report.html
Generated Allure results: reports/allure-results/
```

---

## 🤝 Contributing

Feel free to fork this project, add your own page objects, integrate new test suites, or enhance the CI/CD setup!

---

## 📄 License

MIT License - Use this freely in commercial or personal projects.

---
