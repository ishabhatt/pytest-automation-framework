from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_manager import DriverManager

class PageFactory:
	_instances = {}

	@classmethod
	def get_login_page(cls):
		if "login_page" not in cls._instances:
			cls._instances["login_page"] = LoginPage(DriverManager.get_driver())
		return cls._instances["login_page"]

	@classmethod
	def get_inventory_page(cls):
		if "inventory_page" not in cls._instances:
			cls._instances["inventory_page"] = InventoryPage(DriverManager.get_driver())
		return cls._instances["inventory_page"]

	@classmethod
	def reset(cls):
		cls._instances = {}