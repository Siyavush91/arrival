"""
This module contains shared fixtures for UI tests.
"""

import json
import allure
import pytest
import requests
from selenium.webdriver import Chrome, Firefox
from helpers.settings import BASE_HOST, DEVICES_TABLE_HOST
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


# Browser Fixtures
@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def session_vars():
    session_vars = {
        "address": '',
        "type": '',
        "name": '',
        "address-1": '',
        "type-1": '',
        "name-1": '',
        "address-2": '',
        "type-2": '',
        "name-2": '',
        "address-3": '',
        "type-3": '',
        "name-3": '',
        "address-4": '',
        "type-4": '',
        "name-4": '',
        "address-5": '',
        "type-5": '',
        "name-5": '',
        "freq1": '',
        "freq2": '',
        "duty1": '',
        "duty2": '',
        "repId": '',
    }
    return session_vars


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture
def browser(request, config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    # open browser fullscreen
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            # Attaching screenshot to Allure
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore

    # For cleanup, quit the driver
    def fin():
        driver.close()
    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def get_devices_attribute(session_vars):
    """
    Get devices attributes: address, name, type
    """
    response = requests.get(DEVICES_TABLE_HOST).json()
    session_vars['attributes'] = (response[0]['address'], response[0]['type'], response[0]['name'])
    session_vars['attributes-1'] = (response[1]['address'], response[1]['type'], response[1]['name'])
    session_vars['attributes-2'] = (response[2]['address'], response[2]['type'], response[2]['name'])
    session_vars['attributes-3'] = (response[3]['address'], response[3]['type'], response[3]['name'])
    session_vars['attributes-4'] = (response[4]['address'], response[4]['type'], response[4]['name'])


@pytest.fixture(scope="session")
def get_devices_pmw(session_vars):
    """
    Get devices PMW: Duty, Frequency
    """
    response = requests.get(DEVICES_TABLE_HOST).json()
    session_vars['pin1'] = (response[0]['pin_1_pwm_d'], response[0]['pin_1_pwm_f'])
    session_vars['pin2'] = (response[0]['pin_2_pwm_d'], response[0]['pin_2_pwm_f'])
    session_vars['pin3'] = (response[1]['pin_1_pwm_d'], response[1]['pin_1_pwm_f'])
    session_vars['pin4'] = (response[1]['pin_2_pwm_d'], response[1]['pin_2_pwm_f'])
