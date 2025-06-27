from http import HTTPStatus


def test_root_should_return_200(test_client):
    response = test_client.get('/')

    assert response.status_code == HTTPStatus.OK
