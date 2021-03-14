import requests
import pytest

class APIClient:
    headers = {}

    def __init__(self, address='http://localhost:5585'):
        self.address = address

    def do_get(self, endpoint, data=None):
        url = "/".join([self.address, endpoint])
        return requests.get(url, data, headers=self.headers)

    def do_post(self, endpoint, data=None):
        url = "/".join([self.address, endpoint])
        headers = self.headers
        headers["Content-type"] = "application/json"
        return requests.post(url, data, headers=headers)

    def do_patch(self, endpoint, data=None, **kwargs):
        url = "/".join([self.address, endpoint])
        return requests.patch(url, data, **kwargs)
