import pytest
from pages.page_factory import PageFactory
from selenium.webdriver.common.by import By

@pytest.mark.regression
def test_cart_navigation(browser, config):
	PageFactory.get_login_page().load()
	PageFactory.get_login_page().login("standard_user", "secret_sauce")

	PageFactory.get_inventory_page().add_first_item_to_cart()
	PageFactory.get_inventory_page().go_to_cart()
	assert "cart" in browser.current_url