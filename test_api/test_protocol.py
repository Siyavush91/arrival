import pytest

endpoints = ["/devices"]


@pytest.mark.parametrize("endpoint", endpoints)
def test_info(client, endpoint):
    response = client.do_get(endpoint)
    assert response.status_code == 200, 'Wrong status'


@pytest.mark.parametrize("endpoint", endpoints)
def test_headers(client, endpoint):
    response = client.do_get(endpoint)
    assert response.headers['Date'], 'Header date does not exist'
    assert response.headers['Content-Type'] == 'application/json'
    assert response.headers['Content-Length'] == "587"


@pytest.mark.parametrize("endpoint", endpoints)
def test_not_found(client, endpoint):
    response = client.do_get(f'{endpoint}/test')
    assert response.status_code == 404, 'Wrong status'
