class DriverManager:
	_driver = None

	@classmethod
	def set_driver(cls, driver):
		cls._driver = driver

	@classmethod
	def get_driver(cls):
		if cls._driver is None:
			raise RuntimeError("WebDriver not set. Call set_driver() first.")
		return cls._driver

	@classmethod
	def quit_driver(cls):
		if cls._driver:
			cls._driver.quit()
			cls._driver = None