import pytest
from helpers import constants

endpoints = ["/devices"]

positive_test_data = [
    ["4A", 0, 1, 9, 10],
    ["4A", 19, 50, 100, 500]
]

invalid_freq_type_data = [
    ["65", 99, -1, 11, 500]
]

invalid_freq_diapason_data = [
    ["65", 99, 0, 11, 500],
    ["65", 20, 50, 11, 501]
]

invalid_duty_diapason_data = [
    ["4A", 101, 20, 50, 0]
]

invalid_duty_type_data = [
    ["65", 99, -1, 11, 500]
]

not_exist_address_data = [
    ["65", 99, -1, 11, 500]
]


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", positive_test_data)
def test_update_pmw_value(client, endpoint, address, duty1, freq1, duty2, freq2):
    payload = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
    response = client.do_patch(endpoint, params=payload)
    response_two = client.do_get(endpoint).json()
    assert response_two[0]["pin_1_pwm_d"] == duty1, f'PMW not changed'
    assert response_two[0]["pin_1_pwm_f"] == freq1, f'PMW not changed'
    assert response_two[0]["pin_2_pwm_d"] == duty2, f'PMW not changed'
    assert response_two[0]["pin_2_pwm_f"] == freq2, f'PMW not changed'
    assert response.text == 'OK', "Wrong message"


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", invalid_duty_diapason_data)
def test_invalid_duty_diapason(client, endpoint, address, duty1, freq1, duty2, freq2):
    payload = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
    response = client.do_patch(endpoint, params=payload)
    assert response.text[32:] == constants.MSG_INVALID_DUTY_DIAPASON[32:]


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", invalid_freq_type_data)
def test_invalid_freq_value(client, endpoint, address, duty1, freq1, duty2, freq2):
    payload = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
    response = client.do_patch(endpoint, params=payload)
    response_two = client.do_get(endpoint).json()
    assert response.text == constants.MSG_INVALID_FREQ_ONE


@pytest.mark.parametrize("endpoint", endpoints)
@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", invalid_freq_diapason_data)
def test_invalid_freq_diapason(client, endpoint, address, duty1, freq1, duty2, freq2):
    payload = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
    data = {'address': '65', 'duty1': 100, "freq1": 100, 'duty2': 100, "freq2": 100}
    client.do_patch(endpoint, params=data)
    response = client.do_patch(endpoint, params=payload)
    response_two = client.do_get(endpoint).json()
    assert response_two[1]["pin_1_pwm_f"] != freq1, f'PMW changed'
    assert response_two[1]["pin_2_pwm_f"] != freq2, f'PMW changed'
    assert response.text[32:] == constants.MSG_INVALID_FREQ_DIAPASON[32:]


@pytest.mark.parametrize("endpoint", endpoints)
def test_no_address(client, endpoint):
    payload = {'duty1': 100, "freq1": 10, 'duty2': 100, "freq2": 500}
    response = client.do_patch(endpoint, params=payload)
    assert response.text == constants.MSG_NO_ADDRESS
    assert response.status_code == 400


@pytest.mark.parametrize("endpoint", endpoints)
def test_address_dont_exist(client, endpoint):
    payload = {'duty1': 100, "freq1": 10, 'duty2': 100, "freq2": 500}
    response = client.do_patch(endpoint, params=payload)
    assert response.text == constants.MSG_NO_ADDRESS
    assert response.status_code == 400
