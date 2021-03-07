import pytest
from helpers import constants

endpoints = ["/devices"]


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address", ["4A", "65"])
@pytest.mark.parametrize("duty1", [0, 9, 100])
@pytest.mark.parametrize("duty2", [1, 11, 99])
@pytest.mark.parametrize("freq1", [0])
@pytest.mark.parametrize("freq2", [500])
def test_change_value(client, endpoint, address, duty1, duty2, freq1, freq2):
    payload = {'address': address, 'duty1': duty1, "freq1": duty2, 'duty2': freq1, "freq2": freq2}
    response = client.do_patch(endpoint, params=payload)
    assert response.status_code == 200
    assert isinstance(response.text, str)


@pytest.mark.parametrize("endpoint", endpoints)
def test_change_to_not_correct_value_(client, endpoint):
    payload = {'address': '3F', 'duty1': 200, "freq1": 500, 'duty2': 100, "freq2": 500}
    response = client.do_patch(endpoint, params=payload)
    assert response.text == constants.MSG_INVALID_VALUE


