# 🚀 Pytest + Selenium + Allure Automation Framework (Dockerized)

This repository contains a complete end-to-end automation testing framework using:

- ✅ Python + Pytest
- ✅ Selenium WebDriver
- ✅ Allure Reports
- ✅ Docker (Headless Chrome)
- ✅ Page Object Model (POM)
- ✅ Screenshot on failure (saved to disk + attached to report)
- ✅ GitHub Actions CI integration

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