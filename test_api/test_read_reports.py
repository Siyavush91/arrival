import pytest


address_doesnt_exist = [
    ["100", 100]
]


def test_requesting_service_reports(client, create_data_for_report_test):
    for address, rep_id in create_data_for_report_test:
        response = client.get_report(address, rep_id)
        assert response.status_code == 200, "Wrong status"


@pytest.mark.parametrize("address, rep_id", address_doesnt_exist)
def test_device_address_doesnt_exist(client, address, rep_id):
    response = client.get_report(address, rep_id)
    assert response.status_code == 400, 'Report requested without device address'
