import json
import requests


class APIClient:
    def __init__(self, url='http://localhost:5585'):
        self.url = url

    def get_report(self, address: str = None, rep_id: int = None):
        report = {"repId": rep_id, 'address': address,}
        request = requests.get(f'{self.url}/report', params=report)
        return request

    def get_all_devices(self) -> list:
        devices_url = f'{self.url}/devices'
        request = requests.get(devices_url)
        return json.loads(request.content)

    def get_device_by_address(self, address: str = None) -> dict:
        all_devices = self.get_all_devices()
        new_pmw = next((device for device in all_devices if device['address'] == address), None)
        return new_pmw

    def update_device_pmw(self, address: str = None, duty1: int = None, freq1: int = None, duty2: int = None,
                   freq2: int = None):
        device_pmw = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
        response = requests.patch(f'{self.url}/devices', params=device_pmw)
        return response

    def set_device_pmw_to_default(self, address: str = None):
        device_pmw = {'address': address, 'duty1': 100, "freq1": 100, 'duty2': 100, "freq2": 100}
        request = requests.patch(f'{self.url}/devices', params=device_pmw)
        return request
