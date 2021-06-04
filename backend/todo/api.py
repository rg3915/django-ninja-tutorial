from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from .models import Todo

router = Router()

# TodoSchema = create_schema(Todo, depth=1)
TodoSchema = create_schema(Todo)


@router.get("/todos", response=List[TodoSchema])
def list_todos(request):
    qs = Todo.objects.all()
    return qs


@router.get("/todos/{id}", response=TodoSchema)
def get_todo(request, id: int):
    todo = get_object_or_404(Todo, id=id)
    return todo
