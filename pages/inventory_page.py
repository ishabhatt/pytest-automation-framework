from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class InventoryPage(BasePage):
	SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
	CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
	CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
	CART_CONTINUE_SHOPPING = (By.ID, "continue-shopping")
	INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
	INVENTORY_NAMES = (By.CLASS_NAME, "inventory_item_name")
	ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
	REMOVE_FROM_CART_BUTTONS = (By.XPATH, "//button[text()='Remove']")

	@allure.step("Get all product names from inventory")
	def get_item_names(self):
		return [el.text for el in self.driver.find_elements(*self.INVENTORY_NAMES)]

	@allure.step("Add first product to cart")
	def add_first_item_to_cart(self):
		# Get all add-to-cart buttons
		buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

		if not buttons:
			raise Exception("No 'Add to cart' buttons found.")

		# Click the first one
		print(f"Clicked button: {buttons[0].text}")
		buttons[0].click()
		print(f"Clicked button: {buttons[0].text}")

		# Now wait for ANY remove button to appear
		WebDriverWait(self.driver, self.timeout).until(
			lambda driver: driver.find_elements(*self.REMOVE_FROM_CART_BUTTONS)
		)

	@allure.step("Get cart item count")
	def get_cart_count(self):
		return self.get_text(self.CART_BADGE) if self.is_visible(self.CART_BADGE) else "0"

	@allure.step("Navigate to cart")
	def go_to_cart(self):
		self.click(self.CART_ICON)
		self.wait_until_clickable(self.CART_CONTINUE_SHOPPING)

	@allure.step("Sort products by: {value}")
	def sort_products(self, value):
		dropdown = self.find(self.SORT_DROPDOWN)
		dropdown.click()
		dropdown.find_element(By.XPATH, f"//option[@value='{value}']").click()