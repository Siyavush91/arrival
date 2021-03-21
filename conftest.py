"""
This module contains shared fixtures for UI tests.
"""
import os
import json
import allure
import pytest
import requests
import datetime
import logging
from selenium.webdriver import Firefox
from helpers.settings import DEVICES_TABLE_HOST
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

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
        "device": '',
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
    driver = EventFiringWebDriver(driver, WdListener())

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


class WdListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        dirname = os.path.dirname(__file__)
        now = datetime.datetime.now()
        img_name = now.strftime("%Y-%m-%d_%H-%m-%S") + '_img.png'
        img_path = os.path.join(dirname, 'screenshots', img_name)
        message = str(now) + driver.name + "_" + exception.msg
        driver.save_screenshot(img_path)
        allure.attach.file(img_path, attachment_type=allure.attachment_type.PNG)
        logging.error(message)


@pytest.fixture(scope='session')
def get_all_devices() -> list:
    request = requests.get(DEVICES_TABLE_HOST)
    return json.loads(request.content)


@pytest.fixture(scope='session')
def get_number_of_devices() -> int:
    request = requests.get(DEVICES_TABLE_HOST).json()
    number = len(request)
    return number


@pytest.fixture(scope="session")
def get_device_attribute(get_all_devices, get_number_of_devices):
    i = 0
    response = get_all_devices
    attributes_key = ['address','type','name']
    device_attributes = []
    for device in range(i, get_number_of_devices):
        attributes_value = [response[i][x] for x in attributes_key]
        i += 1
        device_attributes.append(attributes_value)
    return device_attributes


@pytest.fixture(scope="session")
def get_devices_attribute(session_vars, get_device_attribute):
    """
    Get devices attributes: address, name, type
    """
    session_vars['device'] = get_device_attribute[0]
    session_vars['device-1'] = get_device_attribute[1]
    session_vars['device-2'] = get_device_attribute[2]
    session_vars['device-3'] = get_device_attribute[3]
    session_vars['device-4'] = get_device_attribute[4]


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
