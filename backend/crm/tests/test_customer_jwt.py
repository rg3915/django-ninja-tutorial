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


@pytest.fixture
def get_tokens_for_user(create_user):
    # https://eadwincode.github.io/django-ninja-jwt/creating_tokens_manually/
    from ninja_jwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(create_user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.mark.django_db
def test_list_customer(auto_login_user, get_tokens_for_user, client):
    # from ninja_jwt.authentication import JWTAuth
    # from datetime import timedelta

    user = auto_login_user()

    # expiration_time = timedelta(days=1)
    # access_token = JWTAuth().create_access_token(data={"sub": str(user.id)}, expires_time=expiration_time)
    access_token = get_tokens_for_user

    headers = {"Authorization": f"Bearer {access_token['access']}"}
    response = client.get("/api/v1/crm/customers", headers=headers)

    assert response.status_code == HTTPStatus.OK
