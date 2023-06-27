from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]