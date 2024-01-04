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
    return "strong-test-pass"


@pytest.fixture
def create_user(django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client

    return make_auto_login


@pytest.mark.django_db
def test_list_customer(client, auto_login_user):
    client = auto_login_user()
    response = client.get("/api/v1/crm/customer")
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_create_customer(auto_login_user, customer_data):
    client = auto_login_user()
    response = client.post(
        "/api/v1/crm/customer", customer_data, content_type="application/json"
    )

    expected = {
        "id": 1,
        "first_name": "Regis",
        "last_name": "Santos",
        "created_by": 1,
    }

    assert response.status_code == HTTPStatus.CREATED
    assert expected == json.loads(response.content)


@pytest.mark.django_db
def test_create_customer_created_by_id_3(auto_login_user, customer_data):
    _ = auto_login_user()
    _ = auto_login_user()
    client = auto_login_user()
    response = client.post(
        "/api/v1/crm/customer", customer_data, content_type="application/json"
    )

    expected = {
        "id": 1,
        "first_name": "Regis",
        "last_name": "Santos",
        "created_by": 3,
    }

    assert response.status_code == HTTPStatus.CREATED
    assert expected == json.loads(response.content)
