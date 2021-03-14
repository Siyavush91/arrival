from pages.BasePage import BasePage
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
        table_device_row = (By.XPATH, f"//tr[@data-row-key='{device_address}']//button")
        return self._find_elements(table_device_row)[0].click()

    def go_to_diagnostics_page(self, device_address: str):
        device_row = (By.XPATH, f"//tr[@data-row-key='{device_address}']//button")
        return self._find_elements(device_row)[1].click()
