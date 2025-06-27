from http import HTTPStatus

from fastapi_zero.schemas import UserSchemaResponse


def test_create_user_should_return_201(test_client):
    response = test_client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'test@email.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['username'] == 'test'


def test_should_return_users_list(test_client, user, token):
    user_schema = UserSchemaResponse.model_validate(user).model_dump()
    response = test_client.get(
        '/users/', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user_should_return_200(test_client, user, token):
    test_client.post(
        '/users/',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    response = test_client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT


def test_delete_user_should_return_200(test_client, user, token):
    response = test_client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'User deleted'}
