from django.contrib import admin
from django.urls import path, include
from calculator import views
urlpatterns = [
    path('', views.calculator, name = "name"),   
]
