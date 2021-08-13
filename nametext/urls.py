
from django.urls import path,include
from django.contrib import admin
from .views import name


urlpatterns =[
    path('',name),
]