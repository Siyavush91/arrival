import pytest
from .api_client import APIClient
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:5585")


@pytest.fixture
def client(request):
    return APIClient(request.config.getoption("--url"))


@pytest.fixture
def create_data_for_report_test():
    """
    Get response with all devices and return all combination of address, rep_id in list
    """
    response = requests.get('http://localhost:5585/devices').json()
    attributes_key = ['address']
    rep_id = [100, 200, 300, 400]
    result = []
    for index, item in enumerate(response):
        attributes = [item[x] for x in attributes_key]
        for rep in rep_id:
            attributes_list = attributes.copy()
            attributes_list.insert(0, rep)
            result.append(attributes_list)
    return result
