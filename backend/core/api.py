from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from django.contrib.auth.models import User, Group

router = Router()

GroupSchema = create_schema(Group, fields=['id', 'name'])

UserSchema = create_schema(User, custom_fields=[
    ('groups', List[GroupSchema], None),
])


@router.get("/users", response=List[UserSchema])
def list_users(request):
    qs = User.objects.exclude(username='admin')
    return qs


@router.get("/users/{id}", response=UserSchema)
def get_user(request, id: int):
    user = get_object_or_404(User, id=id)
    return user
