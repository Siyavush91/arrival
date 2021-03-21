import pytest

positive_test_data = [
    ["4A", 100],
    ["65", 200],
    ["80", 300],
    ["3F", 400]
]

address_doesnt_exist = [
    ["100", 100]
]


@pytest.mark.parametrize("address, rep_id", positive_test_data)
def test_requesting_service_reports(client, address, rep_id):
    response = client.get_report(address, rep_id)
    assert response.status_code == 200, "Wrong status"


@pytest.mark.parametrize("address, rep_id", address_doesnt_exist)
def test_device_address_doesnt_exist(client, address, rep_id):
    response = client.get_report(address, rep_id)
    assert response.status_code == 400, 'Report requested without device address'
