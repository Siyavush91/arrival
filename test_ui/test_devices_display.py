from pages.main_page import MainPO
from helpers.settings import BASE_HOST


def test_display_devices_list_by_attributes(browser, create_devices_dict, session_vars):
    browser.get(BASE_HOST)
    page = MainPO(browser)
    for device in session_vars['devices']:
        page.verify_device(*device)
