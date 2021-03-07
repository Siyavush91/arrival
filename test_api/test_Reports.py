import pytest

endpoints = ['/report']

@pytest.mark.parametrize("endpoint", endpoints)
def test_api_info_msg_check(client, endpoint):
    """
    API предоставляет информацию о доступных устройствах в сети
    """
    payload = {'address': "4A", 'repId': ""}
    response = client.do_get(endpoint, data=payload)
    assert response.text == "Invalid type of 'repId' value"


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address", ["4A", "65", "80", "3F", "40"])
@pytest.mark.parametrize("repId", [100, 200, 300, 400])
def test_api_base_check_report(client, endpoint, address, repId):
    """

    """
    payload = {'address': address, 'repId': repId}
    response = client.do_get(endpoint, data=payload)
    assert response.status_code == 200
    assert isinstance(response.text, str)
