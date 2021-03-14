# import pytest
# from helpers import constants
#
# endpoints = ["/devices"]
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# @pytest.mark.parametrize("address", ["4A"])
# @pytest.mark.parametrize("duty1", [0, 9, 100])
# @pytest.mark.parametrize("duty2", [1, 11, 99])
# @pytest.mark.parametrize("freq1", [1, 100])
# @pytest.mark.parametrize("freq2", [10, 500])
# def test_change_value(client, endpoint, address, duty1, duty2, freq1, freq2):
#     payload = {'address': address, 'duty1': duty1, "freq1": freq1, 'duty2': duty2, "freq2": freq2}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.status_code == 200
#     assert response.text == 'OK'
#     assert isinstance(response.text, str)
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# def test_change_to_not_correct_value_(client, endpoint):
#     payload = {'address': '3F', 'duty1': 101, "freq1": 10, 'duty2': 100, "freq2": 500}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.text == constants.MSG_INVALID_DUTY
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# def test_change_to_not_correct_value_(client, endpoint):
#     payload = {'address': '3F', 'duty1': 0, "freq1": 0, 'duty2': 99, "freq2": 500}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.text == constants.MSG_INVALID_FREQ
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# def test_change_to_not_correct_value_(client, endpoint):
#     payload = {'address': '100', 'duty1': 100, "freq1": 10, 'duty2': 100, "freq2": 500}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.text == constants.MSG_INVALID_DUTY
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# @pytest.mark.parametrize("address", ["80"])
# @pytest.mark.parametrize("duty2", [0, 9, 100])
# @pytest.mark.parametrize("freq2", [1, 100])
# def test_change_pin_one_value(client, endpoint, address, duty2, freq2):
#     payload = {'address': address, 'duty2': duty2, "freq2": freq2}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.status_code == 200
#     assert response.text == 'OK'
#     assert isinstance(response.text, str)
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# @pytest.mark.parametrize("address", ["80"])
# @pytest.mark.parametrize("duty1", [0.1, 0.9, 0.100])
# @pytest.mark.parametrize("freq1", [1, 0.1])
# def test_change_pin_two_value(client, endpoint, address, duty1, freq1):
#     payload = {'address': address, 'duty1': duty1, "freq1": freq1}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.status_code == 200
#     assert response.text == constants.MSG_INVALID_DUTY_ONE
#     assert isinstance(response.text, str)
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# @pytest.mark.parametrize("address", ["80"])
# @pytest.mark.parametrize("duty1", [0, 9, 100])
# @pytest.mark.parametrize("freq2", [1, 100])
# def test_change_cross_value(client, endpoint, address, duty1, freq2):
#     payload = {'address': address, 'duty1': duty1, "freq1": freq2}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.status_code == 200
#     assert isinstance(response.text, str)
#
#
# @pytest.mark.parametrize("endpoint", endpoints)
# def test_change_to_not_correct_value(client, endpoint):
#     payload = {'address': '100', 'duty1': 100, "freq1": 10, 'duty2': 100, "freq2": 500}
#     response = client.do_patch(endpoint, params=payload)
#     assert response.status_code == 500
#     assert response.text == constants.MSG_INVALID_ADDRESS
