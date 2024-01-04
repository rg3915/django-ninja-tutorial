import uuid
import json
from http import HTTPStatus

import pytest


@pytest.fixture
def customer_data():
    return {
        "first_name": "Regis",
        "last_name": "Santos",
    }


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(django_user_model, test_password):
    '''
    Cria usuário.
    '''
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_return_user(client, create_user, test_password):
    '''
    Faz login. E retorna o client e o usuário.
    '''
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login


def get_token(client, user):
    data = {
        'username': user.username,
        'password': 'strong-test-pass',
    }

    response = client.post(
        '/api/v1/token/pair', data, content_type='application/json'
    )

    return json.loads(response.content)


@pytest.mark.django_db
def test_list_customers_with_token(auto_login_return_user):
    client, user = auto_login_return_user()

    test_password = 'strong-test-pass'

    client.login(username=user.username, password=test_password)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.get('/api/v1/crm/customers/jwt', headers=headers)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_create_customer(auto_login_return_user, customer_data):
    client, user = auto_login_return_user()

    test_password = 'strong-test-pass'

    client.login(username=user.username, password=test_password)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.post(
        "/api/v1/crm/customers/jwt",
        customer_data,
        content_type="application/json",
        headers=headers
    )

    expected = {
        "id": 1,
        "first_name": "Regis",
        "last_name": "Santos",
        "created_by": 1,
    }

    assert response.status_code == HTTPStatus.CREATED
    assert expected == json.loads(response.content)
