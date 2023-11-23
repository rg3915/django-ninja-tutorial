from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_list_customer(client):
    response = client.get('/api/v1/crm/customers/')
    assert response.status_code == HTTPStatus.OK


@pytest.fixture
def customer_data():
    return {
        'first_name': 'Regis',
        'last_name': 'Santos'
    }


@pytest.mark.django_db
def test_create_customer(client, customer_data):
    response = client.post('/api/v1/crm/customers/', customer_data)
    assert response.status_code == HTTPStatus.OK
