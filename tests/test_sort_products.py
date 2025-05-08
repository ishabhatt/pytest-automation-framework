import pytest
from pages.page_factory import PageFactory

@pytest.mark.regression
def test_sort_products_a_to_z(browser, config):
	PageFactory.get_login_page().load()
	PageFactory.get_login_page().login("standard_user", "secret_sauce")

	PageFactory.get_inventory_page().sort_products("az")
	item_names = PageFactory.get_inventory_page().get_item_names()
	assert item_names == sorted(item_names)