from django.contrib import admin
from django.urls import path, include
from .views import employee_list

urlpatterns = [
    path('employee', employee_list),
]