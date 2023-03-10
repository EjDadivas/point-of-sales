from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_view, name="item_view"),
    path('list_item', views.list_item, name="list_item"),
    path('add_item', views.add_item, name="add_item"),
    path('delete_item/<int:pk>', views.delete_item, name="delete_item"),
    path('update_item/<int:pk>', views.update_item, name="update_item")
]
