from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPO(BasePage):
    devices_table = (By.CLASS_NAME, "ant-row")
    table_head_row = (By.CLASS_NAME, "ant-table-thead")

    def verify_device(self, device_address: str, device_type: str, device_name: str):
        table_device_row = (By.XPATH, f"//tr[@data-row-key='{device_address}']//descendant::td[text()='{device_name}']"
                                      f"//following-sibling::td[text()='{device_type}']")
        self._wait_element_displayed(table_device_row)
        return self

    def waiter(self):
        self._wait_element_displayed(self.devices_table)
        return self

    def go_to_monitoring_page(self, device_address: str):
        element = (By.XPATH, f"//tr[@data-row-key='{device_address}']//button")
        monitoring_btn = self._find_elements(element)[0]
        monitoring_btn.click()
        return self


    def go_to_diagnostics_page(self, device_address: str):
        element = (By.XPATH, f"//tr[@data-row-key='{device_address}']//button")
        diagnostics_btn = self._find_elements(element)[1]
        diagnostics_btn.click()
        return self
