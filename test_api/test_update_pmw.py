import pytest
from helpers import constants

positive_test_data = [
    ["4A", 0, 1, 9, 10],
    ["65", 19, 50, 100, 500]
]

invalid_freq_type_data = [
    ["65", 99, -1, 11, 500, 1]
]

invalid_freq_value = [
    ["65", 99, 0, 11, 500, 1],
    ["65", 20, 50, 11, 501, 2]
]

invalid_freq_diapason_data = [
    ["65", 99, 300, 11, 500, 1],
    ["65", 20, 50, 11, 400, 2]
]

invalid_duty_diapason_data = [
    ["4A", 101, 20, 50, 0, 1],
    ["4A", 0, 20, - 1, 200, 2]
]

invalid_duty_type_data = [
    ["65", 99, -1, 11, 500]
]

not_exist_address_data = [
    ["100", 99, -1, 11, 500]
]


@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", positive_test_data)
def test_update_pmw_value(client, address, duty1, freq1, duty2, freq2):
    new_pmw = client.update_device_pmw(address, duty1, freq1, duty2, freq2)
    current_pmw = client.get_device_by_address(address)
    assert new_pmw.status_code == 200, 'Wrong status'
    assert current_pmw["pin_1_pwm_d"] == duty1, 'Duty1 PMW not changed'
    assert current_pmw["pin_1_pwm_f"] == freq1, 'Freq1 PMW not changed'
    assert current_pmw["pin_2_pwm_d"] == duty2, 'Duty2 PMW not changed'
    assert current_pmw["pin_2_pwm_f"] == freq2, 'Freq2 PMW not changed'


@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2, duty_pmw_num", invalid_duty_diapason_data)
def test_invalid_duty_diapason(client, address, duty1, freq1, duty2, freq2, duty_pmw_num):
    new_pmw = client.update_device_pmw(address, duty1, freq1, duty2, freq2)
    assert new_pmw.text == constants.MSG_INVALID_DUTY_DIAPASON.format(duty_pmw_num)


@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2, freq_pmw_num", invalid_freq_diapason_data)
def test_invalid_freq_diapason(client, address, duty1, freq1, duty2, freq2, freq_pmw_num):
    request = client.set_device_pmw_to_default(address)
    assert request.status_code == 200
    new_pmw = client.update_device_pmw(address, duty1, freq1, duty2, freq2)
    assert new_pmw.text == constants.MSG_INVALID_FREQ_DIAPASON.format(freq_pmw_num)


@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2, pmw_num", invalid_freq_value)
def test_pmw_not_change_with_invalid_freq_value(client, address, duty1, freq1, duty2, freq2, pmw_num):
    request = client.set_device_pmw_to_default(address)
    assert request.status_code == 200
    client.update_device_pmw(address, duty1, freq1, duty2, freq2)
    current_pmw = client.get_device_by_address(address)
    assert current_pmw["pin_1_pwm_d"] != duty1, f'Duty{pmw_num} PMW changed'
    assert current_pmw["pin_1_pwm_f"] != freq1, f'Freq{pmw_num} PMW changed'
    assert current_pmw["pin_2_pwm_d"] != duty2, f'Duty{pmw_num} PMW changed'
    assert current_pmw["pin_2_pwm_f"] != freq2, f'Freq{pmw_num} PMW changed'


@pytest.mark.parametrize("address, duty1, freq1, duty2, freq2", not_exist_address_data)
def test_address_doesnt_exist(client, address, duty1, freq1, duty2, freq2):
    new_pmw = client.update_device_pmw(address, duty1, freq1, duty2, freq2)
    assert new_pmw.status_code == 400
    assert new_pmw.text == constants.MSG_ADDRESS_DONT_EXIST
