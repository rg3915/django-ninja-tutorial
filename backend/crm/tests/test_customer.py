from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_list_customer(client):
    response = client.get('/api/v1/crm/customers/')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_customer(client):
    response = client.get('/api/v1/crm/customers/')
    assert response.status_code == HTTPStatus.OK
