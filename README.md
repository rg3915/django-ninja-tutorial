# Django Ninja Tutorial

Este é um tutorial do [Django Ninja](https://django-ninja.rest-framework.com/) usado na [Live](https://youtu.be/cZ7n3HN9MiU) no YouTube.

Frontend com VueJS: https://github.com/rg3915/regisdopython-vue

![vuejs_django_ninja.png](img/vuejs_django_ninja.png)

![fullstack-diagrama-frontend-backend-final3.png](img/fullstack-diagrama-frontend-backend-final3.png)


## Construindo uma API com Django Ninja

https://django-ninja.rest-framework.com/tutorial/


```
pip install django-ninja
```

```python
# api.py
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/ping")
def ping(request):
    return "pong"
```

```python
# urls.py
from django.contrib import admin
from django.urls import path

from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
```


## Este projeto foi feito com:

* [Python 3.9.4](https://www.python.org/)
* [Django 3.2.4](https://www.djangoproject.com/)
* [Django Ninja 0.13.1](https://www.django-rest-framework.org/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-ninja-tutorial.git
cd django-ninja-tutorial
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

Define `api = NinjaAPI(csrf=True)` em `backend/api.py`.


## Swagger

http://localhost:8000/api/v1/docs



## Frontend

Editar rota

```
fetch('http://127.0.0.1:8000/api/v1/core/users')
```


