from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('', include('lists.urls'), name='lists-urls')
]

