from pages.main_page import MainPO
from helpers.settings import BASE_HOST


def test_display_devices_list_by_attributes(browser, get_devices_attribute, session_vars):
    browser.get(BASE_HOST)
    MainPO(browser).verify_device(*session_vars['device']) \
        .verify_device(*session_vars['device-1']) \
        .verify_device(*session_vars['device-2']) \
        .verify_device(*session_vars['device-3']) \
        .verify_device(*session_vars['device-4'])
