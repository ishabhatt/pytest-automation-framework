import sys
import os
import pytest
import allure
from allure_commons.types import Severity
from pages.page_factory import PageFactory
from utils.data_loader import load_json_data

test_data = load_json_data("login_test_data.json")

@allure.severity(Severity.CRITICAL)
@pytest.mark.smoke
@pytest.mark.parametrize("data", test_data)
@allure.title("Login test with user: {test_data[username]}")
#@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_login(browser, data):
	PageFactory.get_login_page().load()
	PageFactory.get_login_page().login(data["username"], data["password"])
	
	if data["expected"] == "success":
		assert PageFactory.get_login_page().is_logged_in_successfully()
	elif data["expected"] == "failure":
		assert not PageFactory.get_login_page().is_logged_in_successfully()
		assert data["error"] in PageFactory.get_login_page().get_error_message()
