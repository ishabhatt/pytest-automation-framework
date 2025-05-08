import pytest
from pages.page_factory import PageFactory
import logging

@pytest.mark.smoke
def test_add_to_cart_updates_badge(browser, config):
	PageFactory.get_login_page().load()
	PageFactory.get_login_page().login("standard_user", "secret_sauce")

	PageFactory.get_inventory_page().add_first_item_to_cart()
	assert PageFactory.get_inventory_page().get_cart_count() == "1"