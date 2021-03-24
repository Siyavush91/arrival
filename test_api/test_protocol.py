import requests
from helpers.settings import BASE_HOST


def test_info():
    response = requests.get(BASE_HOST)
    assert response.status_code == 200, 'Wrong status'


def test_header():
    response = requests.get(BASE_HOST)
    content_length = str(len(response.text))
    assert response.headers['Content-Length'] == content_length


def test_not_found():
    response = requests.get(f'{BASE_HOST}/test')
    assert response.status_code == 404, 'Wrong status'
