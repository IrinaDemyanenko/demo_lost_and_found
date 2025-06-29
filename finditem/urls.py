"""Маршрутизация."""
from django.urls import path
from finditem.views import find_item_view


urlpatterns = [
    path('', find_item_view, name='find-item'),  # форма поиска и ответ
]
