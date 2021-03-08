from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MainPO(BasePage):
    devices_table =  (By.CLASS_NAME, "ant-row")
    table_head_row = (By.CLASS_NAME, "ant-table-thead")
    table_engine_row = (By.CSS_SELECTOR, '[data-row-key="4A"]')
    table_power_row = (By.CSS_SELECTOR, '[data-row-key="65"]')
    table_transmission_row = (By.CSS_SELECTOR, '[data-row-key="80]')
    table_brake_row = (By.CSS_SELECTOR, '[data-row-key="3F"]')
    buttons = (By.CLASS_NAME, "ant-btn-primary")

    def verify_page(self):
        self._wait_for_elements_present([self.devices_table, self.table_head_row, self.table_brake_row, self.table_engine_row, self.table_transmission_row])
        return

    def waiter(self):
        self._wait_element_displayed(self.devices_table)

    def verify_table_header(self):
        text = self._get_element_text(self.table_head_row)
        return text

    def go_to_engine_monitoring(self):
        button_list = self._find_elements(self.buttons)
        button_list[0].click()
        return
