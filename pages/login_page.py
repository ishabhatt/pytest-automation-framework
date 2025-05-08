from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
	USERNAME_INPUT = (By.ID, "user-name")
	PASSWORD_INPUT = (By.ID, "password")
	LOGIN_BUTTON = (By.ID, "login-button")
	ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container")

	def load(self):
		self.visit(self.URL)

	@property
	def URL(self):
		return "https://www.saucedemo.com/"

	def login(self, username, password):
		self.enter_username(username)
		self.enter_password(password)
		self.submit()
		assert "inventory.html" in self.driver.current_url

	@allure.step("Enter Username: {username}")
	def enter_username(self, username):
		element = self.find(self.USERNAME_INPUT)
		element.clear()
		element.send_keys(username)

	@allure.step("Enter Password")
	def enter_password(self, password):
		element = self.find(self.PASSWORD_INPUT)
		element.clear()
		element.send_keys(password)

	@allure.step("Click Login")
	def submit(self):
		self.find(self.LOGIN_BUTTON).click()

	@allure.step("Verify Login Successful")
	def is_logged_in_successfully(self):
		return "inventory.html" in self.driver.current_url

	@allure.step("Verify Login Error")
	def get_error_message(self):
		if self.is_visible(self.ERROR_MSG):
			return self.get_text(self.ERROR_MSG)
		return ""
