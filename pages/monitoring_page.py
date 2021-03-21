from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MonitoringPO(BasePage):

    def verify_pin_one_pmw(self, pin_1_pwm_d: int, pin_1_pwm_f: int):
        table_device_row = (By.XPATH, f"//div[@class='ant-card']//following::input[@value={pin_1_pwm_d}]"
                                      f"//following::span[@title={pin_1_pwm_f}]")
        self._wait_element_displayed(table_device_row)
        return self

    def verify_pin_two_pmw(self, pin_2_pwm_d: int, pin_2_pwm_f: int):
        table_device_row = (By.XPATH, f"//div[@class='ant-card']//following::input[@value={pin_2_pwm_d}]"
                                      f"//following::span[@title={pin_2_pwm_f}]")
        return self._wait_element_displayed(table_device_row)
