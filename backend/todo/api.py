from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from .models import Todo


router = Router(tags=['Todo'])


# TodoSchema = create_schema(Todo, depth=1)
TodoSchema = create_schema(Todo)


class DoneSchemaIn(Schema):
    is_done: bool


@router.get("/todos", response=List[TodoSchema])
def list_todos(request):
    qs = Todo.objects.all()
    return qs


@router.get("/todos/{id}", response=TodoSchema)
def get_todo(request, id: int):
    todo = get_object_or_404(Todo, id=id)
    return todo


@router.put("/todos/{id}/done", response=TodoSchema)
def is_done(request, id: int, payload: DoneSchemaIn):
    todo = get_object_or_404(Todo, id=id)
    todo.is_done = payload.dict().pop('is_done')
    todo.save()
    return todo
