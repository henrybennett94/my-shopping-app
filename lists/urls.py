from django.contrib import admin
from . import views
from django.urls import path, include
from .views import create_shopping_list, open_shopping_list, list_view, add_item

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('my_lists/', list_view, name='list_view'),
    path('create/', create_shopping_list, name='create_shopping_list'),
    path('shopping_list/<int:id>/', open_shopping_list, name='open_shopping_list'),
]

