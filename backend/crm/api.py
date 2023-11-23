from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from .models import Customer


router = Router(tags=['Customers'])


CustomerSchema = create_schema(Customer)


@router.get("/customers", response=list[CustomerSchema])
def list_customers(request):
    return Customer.objects.all()


@router.get("/customers/{id}", response=CustomerSchema)
def get_customer(request, id: int):
    return get_object_or_404(Customer, id=id)
