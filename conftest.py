import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.driver_manager import DriverManager
from pages.page_factory import PageFactory
from utils.config_reader import load_config
import tempfile
import base64
# For embedding screenshots
from py.xml import html
from pytest_html import extras
from datetime import datetime

# ----------------------------
# CLI Hooks for browser/env
# ----------------------------
def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
	parser.addoption("--env", action="store", default="default", help="Environment name from config.yaml")

# ----------------------------
# Load config based on --env
# ----------------------------
@pytest.fixture(scope="session")
def config(request):
	env = request.config.getoption("--env")
	return load_config(env)

# ----------------------------
# Launch browser based on config
# ----------------------------
@pytest.fixture(scope="function")
def browser(request, config):
	browser_type = config["browser"]
	headless = config.get("headless", False)

	if browser_type == "firefox":
		options = FirefoxOptions()
		if headless:
			options.add_argument("--headless")
		driver = webdriver.Firefox(options=options)
	else:
		options = ChromeOptions()
		if headless:
			options.add_argument("--headless=new")
			options.add_argument("--no-sandbox")
			options.add_argument("--disable-dev-shm-usage")
			options.add_argument("--disable-gpu")
			user_data_dir = tempfile.mkdtemp()
			options.add_argument(f"--user-data-dir={user_data_dir}")
		driver = webdriver.Chrome(options=options)

	DriverManager.set_driver(driver)
	driver.implicitly_wait(config.get("implicit_wait", 10))
	driver.maximize_window()
	yield driver
	driver.quit()
	DriverManager.quit_driver()

# ----------------------------
# Clear factory cache
# ----------------------------
@pytest.fixture(autouse=True)
def clear_factory_cache():
	yield
	PageFactory.reset()

# ----------------------------
# Screenshot on failure
# ----------------------------
# Ensure screenshots directory exists
SCREENSHOT_DIR = "./reports/screenshots"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
	"""Hook to capture screenshots and attach them to Allure and pytest-html."""
	outcome = yield
	report = outcome.get_result()

	if report.when == "call" and report.failed:
		browser = item.funcargs.get("browser", None)
		if browser:
			test_name = item.name
			timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
			os.makedirs(SCREENSHOT_DIR, exist_ok=True)

			screenshot_name = f"{test_name}_{timestamp}.png"
			file_path = os.path.join(SCREENSHOT_DIR, screenshot_name)

			# Take screenshot
			screenshot = browser.get_screenshot_as_png()

			# Save screenshot to file
			with open(file_path, "wb") as f:
				f.write(screenshot)

			# Attach to allure
			allure.attach(
				screenshot,
				name=screenshot_name,
				attachment_type=allure.attachment_type.PNG
			)

			# Attach to pytest-html
			extra = getattr(report, "extra", [])
			# Read screenshot as base64
			with open(file_path, "rb") as image_file:
				encoded = base64.b64encode(image_file.read()).decode("utf-8")
			#extra.append(extras.image(src="data:image/png;base64," + encoded, mime_type="image/png"))
			#extra.append(extras.image(file_path))
			html_image = f'<img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:300px;" />'
			extra.append(extras.html(html_image))
			report.extra = extra

			# Add docstring as description
			report.description = str(item.function.__doc__) if item.function.__doc__ else item.name

# ----------------------------
# Embed Screenshot Column in HTML Report
# ----------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
	cells.insert(1, html.th("Description"))
	cells.insert(2, html.th("Status"))
	cells.pop()  # Remove the 'Links' column if unused

def pytest_html_results_table_row(report, cells):
	description = getattr(report, "description", report.nodeid)
	status = "Passed" if report.passed else "Failed" if report.failed else "Skipped"

	cells.insert(1, html.td(description))
	cells.insert(2, html.td(status))
	cells.pop()
