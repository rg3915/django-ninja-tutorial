from django.contrib import admin
from django.urls import include, path

from .api import api

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
