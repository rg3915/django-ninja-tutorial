from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from backend.todo.api import TodoSchema


router = Router(tags=['Users'])


class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    todos: list[TodoSchema]

    class Meta:
        model = User
        fields = '__all__'


@router.get("/users", response=list[UserSchema])
def list_users(request):
    qs = User.objects.exclude(username='admin')
    return qs


@router.get("/users/{id}", response=UserSchema)
def get_user(request, id: int):
    user = get_object_or_404(User, id=id)
    return user
