from http import HTTPStatus
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema
from ninja.orm import create_schema
from ninja_jwt.authentication import JWTAuth
from ninja.security import django_auth

from .models import Customer


router = Router(tags=['Customers'])


CustomerSchema = create_schema(Customer)


class CustomerSchemaIn(ModelSchema):

    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'created_by',
        )


@router.get('/customer', response=list[CustomerSchema], auth=django_auth)
def list_customers(request):
    return Customer.objects.all()


@router.post('/customer', response={HTTPStatus.CREATED: CustomerSchema}, auth=django_auth)
def create_customer(request, payload: CustomerSchemaIn):
    customer = Customer.objects.create(**payload.dict())
    customer.created_by = request.user
    return customer


@router.get('/customer/{id}', response=CustomerSchema, auth=django_auth)
def get_customer(request, id: int):
    return get_object_or_404(Customer, id=id)


@router.get('/customers/jwt', response=list[CustomerSchema], auth=JWTAuth())
def list_customers_jwt(request):
    return Customer.objects.all()


@router.post('/customers/jwt', response={HTTPStatus.CREATED: CustomerSchema}, auth=JWTAuth())
def create_customer_jwt(request, payload: CustomerSchemaIn):
    customer = Customer.objects.create(**payload.dict())
    customer.created_by = request.user
    return customer
