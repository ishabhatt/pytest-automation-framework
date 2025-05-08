from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.timeout = 10

	def visit(self, url):
		self.driver.get(url)

	def find(self, locator):
		return WebDriverWait(self.driver, self.timeout).until(
			EC.presence_of_element_located(locator))

	def click(self, locator):
		self.find(locator).click()

	def type(self, locator, text):
		self.find(locator).clear()
		self.find(locator).send_keys(text)

	def get_text(self, locator):
		return self.find(locator).text

	def is_visible(self, locator):
		try:
			WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
			return True
		except TimeoutException:
			return False

	def wait_until_clickable(self, locator):
		return WebDriverWait(self.driver, self.timeout).until(
			EC.element_to_be_clickable(locator)
		)
