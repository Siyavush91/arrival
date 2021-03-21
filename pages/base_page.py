import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, \
    StaleElementReferenceException
import time
from selenium.webdriver.common.by import By

"""
Base Page comes here.
"""
TIMEOUT=20
DRIVER_TIMEOUT = 1
POLL_FREQUENCY = 0.5

class BasePage:
    """
    Base класс для инициализации базовой страницы, которая будет вызываться всеми остальными страницами.
    """

    def __init__(self, driver = None):
        """
        Инициализация driver.

        """
        self.driver = driver
        self.driver.implicitly_wait(DRIVER_TIMEOUT)
        self.elements_name = {}

    def _wait_to_be_selected(self, *selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(selector))
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False

    def _click_element(self, selector):
        self._wait_to_be_selected(*selector)
        element = self.driver.find_element(*selector)
        element.click()

    def _wait_element_displayed(self, loc):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(loc))
        except TimeoutException:
            error_message = f" Can't find specific element, locator is {loc} "
            raise TimeoutException(error_message)

    def _is_element_visible(self, *selector):
        try:
            return self.driver.find_element(*selector).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False

    def _get_element_text(self, selector):
        e = "No text in element"
        try:
            text = self.driver.find_element(*selector).text
            return text
        except Exception as e:
            return e

    def _wait_for_element_present(self, selector):
        """Wait for an element to become present."""
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            assert(TimeoutException)
        finally:
            # set back to where you once belonged
            self.driver.implicitly_wait(DRIVER_TIMEOUT)

    def _wait_for_elements_present(self, elements):
        for element in elements:
            self._wait_for_element_present(element)

    def _find_elements(self, selector):
        return self.driver.find_elements(*selector)
