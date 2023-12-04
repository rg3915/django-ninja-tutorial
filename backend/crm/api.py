from http import HTTPStatus
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema
from ninja.orm import create_schema

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


@router.get('/customers', response=list[CustomerSchema])
def list_customers(request):
    return Customer.objects.all()


@router.post('/customers', response={HTTPStatus.CREATED: CustomerSchema})
def create_customer(request, payload: CustomerSchemaIn):
    customer = Customer.objects.create(**payload.dict())
    customer.created_by = request.user
    return customer


@router.get('/customers/{id}', response=CustomerSchema)
def get_customer(request, id: int):
    return get_object_or_404(Customer, id=id)
