import pytest
from test_api.api_client import APIClient


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://localhost:5585")

@pytest.fixture
def client(request):
    return APIClient(request.config.getoption("--address"))
