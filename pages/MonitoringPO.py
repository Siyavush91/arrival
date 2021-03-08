from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MonitoringPO(BasePage):
    monitoring_engine_header = (By.CLASS_NAME, "ant-typography")

    def verify_header(self):
        h2 = self._find_elements(self.monitoring_engine_header)
        text = h2[1].text
        # text = self._get_element_text(self.monitoring_engine_header)
        return text
