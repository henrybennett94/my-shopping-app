from django.contrib import admin
from . import views
from django.urls import path, include
from .views import create_shopping_list, open_shopping_list, add_item

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('', include('lists.urls'), name='lists-urls'),
    path('create/', create_shopping_list, name='create_shopping_list'),
    path('list/<int:id>/', open_shopping_list, name='open_shopping_list'),
]

