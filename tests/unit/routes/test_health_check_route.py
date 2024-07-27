import pytest


def test_health_check_then_return_200(client):
    # arrange
    # act
    response = client.get('/healthcheck')

    # assert
    assert response.status_code == 200
    assert response.json()['status'] == 'alive'
    assert response.json()['message'] == 'hello world'
