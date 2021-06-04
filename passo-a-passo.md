# Passo a passo

```
pip install -U pip
pip install django django-ninja django-extensions python-decouple
```


```
pip freeze | grep Django==3.2.4 >> requirements.txt
pip freeze | grep django-extensions >> requirements.txt
pip freeze | grep django-ninja >> requirements.txt
pip freeze | grep python-decouple >> requirements.txt
cat requirements.txt
```

```
django-admin startproject backend .
cd backend
python ../manage.py startapp core
python ../manage.py startapp todo
```

Copiar o [settings_example.py]() e editar o `settings.py`.

```
cp settings_example.py backend/settings.py
```

Editar `core/apps.py`

Editar `todo/apps.py`

```
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

Editar `todo/models.py`

```python
from django.contrib.auth.models import User
# todo/models.py
from django.db import models


class Todo(models.Model):
    title = models.CharField('título', max_length=100)
    description = models.TextField('descrição', null=True, blank=True)
    due_date = models.DateField('data', null=True, blank=True)
    is_done = models.BooleanField('pronto', default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='todos',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'todo'
        verbose_name_plural = 'todos'

    def __str__(self):
        return self.title
```

Editar `todo/admin.py`

```python
# todo/admin.py
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)
```

```
python manage.py makemigrations
python manage.py migrate
```

Rodar o Admin e inserir 2 registros.

Criar as `*/api.py`

```
touch backend/api.py
touch backend/core/api.py
touch backend/todo/api.py
```

Editar `core/api.py`

```python
# core/api.py
from typing import List

from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

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
```

Editar `todo/api.py`

```python
# todo/api.py
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from .models import Todo

router = Router()

TodoSchema = create_schema(Todo, depth=1)


@router.get("/todos", response=List[TodoSchema])
def list_todos(request):
    qs = Todo.objects.all()
    return qs


@router.get("/todos/{id}", response=TodoSchema)
def get_todo(request, id: int):
    todo = get_object_or_404(Todo, id=id)
    return todo
```

Editar `api.py`

```python
# api.py
from ninja import NinjaAPI

from backend.core.api import router as core_router
from backend.todo.api import router as todo_router

api = NinjaAPI()

api.add_router("/core/", core_router)
api.add_router("/todo/", todo_router)
```

Editar `urls.py`

```python
from django.contrib import admin
from django.urls import path

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
```

Entrar em http://localhost:8000/api/v1/docs

