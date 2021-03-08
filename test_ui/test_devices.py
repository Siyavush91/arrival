from pages.MainPO import MainPO
from pages.MonitoringPO import MonitoringPO
from helpers.settings import BASE_HOST
from helpers import constants

def test_devices(browser):
    browser.get(BASE_HOST)
    MainPO(browser).verify_page()
    assert MainPO(browser).verify_table_header() == constants.TABLE_ROW_ONE


def test_devices_two(browser):
    browser.get(BASE_HOST)
    MainPO(browser).waiter()
    MainPO(browser).go_to_engine_monitoring()
    assert MonitoringPO(browser).verify_header() == constants.DIAGNOSTICS_ENGINE_HEADER



