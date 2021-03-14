from pages.MainPO import MainPO
from helpers.settings import BASE_HOST


def test_display_devices_list_by_attributes(browser, get_devices_attribute, session_vars):
    browser.get(BASE_HOST)
    MainPO(browser).verify_device(session_vars['attributes'][0], session_vars['attributes'][1],
                                  session_vars['attributes'][2]) \
        .verify_device(session_vars['attributes-1'][0], session_vars['attributes-1'][1],
                                  session_vars['attributes-1'][2]) \
        .verify_device(session_vars['attributes-2'][0], session_vars['attributes-2'][1],
                                  session_vars['attributes-2'][2]) \
        .verify_device(session_vars['attributes-3'][0], session_vars['attributes-3'][1],
                                  session_vars['attributes-3'][2]) \
        .verify_device(session_vars['attributes-4'][0], session_vars['attributes-4'][1],
                                  session_vars['attributes-4'][2])
