from typing import List

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from backend.todo.api import TodoSchema

router = Router()


class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    todos: List[TodoSchema]

    class Meta:
        model = User
        fields = '__all__'


@router.get("/users", response=List[UserSchema])
def list_users(request):
    qs = User.objects.exclude(username='admin')
    return qs


@router.get("/users/{id}", response=UserSchema)
def get_user(request, id: int):
    user = get_object_or_404(User, id=id)
    return user
