from pages.main_page import MainPO
from pages.monitoring_page import MonitoringPO
from helpers.settings import BASE_HOST
from helpers import constants


def test_display_current_pmw_values_for_first_device(browser, get_devices_attribute, get_devices_pmw, session_vars):
    browser.get(BASE_HOST)
    MainPO(browser).waiter()
    MainPO(browser).go_to_monitoring_page(session_vars['attributes'][0])
    MonitoringPO(browser).verify_pin_one_pmw(session_vars['pin1'][0], session_vars['pin1'][1]) \
        .verify_pin_two_pmw(session_vars['pin2'][0], session_vars['pin2'][1])


def test_display_current_pmw_values_for_second_device(browser, get_devices_attribute, get_devices_pmw, session_vars):
    browser.get(BASE_HOST)
    MainPO(browser).waiter()
    MainPO(browser).go_to_monitoring_page(session_vars['attributes-1'][0])
    MonitoringPO(browser).verify_pin_one_pmw(session_vars['pin3'][0], session_vars['pin3'][1]) \
        .verify_pin_two_pmw(session_vars['pin4'][0], session_vars['pin4'][1])
