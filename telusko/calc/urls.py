from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('calculator',views.home,name='home'),
    path('add',views.add,name='add')
]