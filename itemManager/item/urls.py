from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.item, name="item"),
    path('list_item', views.list_item, name="list_item")
]
