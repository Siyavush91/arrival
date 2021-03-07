import pytest

endpoints = ["/devices"]

@pytest.mark.parametrize("endpoint", endpoints)
def test_api_base_checks(client, endpoint):
    """
    API предоставляет информацию о доступных устройствах в сети
    """
    response = client.do_get(endpoint)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"
    assert isinstance(response.text, str)


@pytest.mark.parametrize("endpoint", endpoints)
def test_device_name(client, endpoint):
    """
    API предоставляет информацию о доступных устройствах в сети
    """
    device_name = ["Engine", "Power", "Transmission", "Brake", "Control"]
    response = client.do_get(endpoint)
    res = response.json()
    name = [device['name'] for device in res]
    assert name == device_name


@pytest.mark.parametrize("endpoint", endpoints)
def test_device_address(client, endpoint):
    """
    API предоставляет информацию о доступных устройствах в сети
    """
    device_address = ["4A", "65", "80", "3F", "40"]
    response = client.do_get(endpoint)
    res = response.json()
    name = [device['address'] for device in res]
    assert name == device_address
