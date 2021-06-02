from django.contrib import admin
from django.urls import path, include
#from .views import employee_list, employee_detail
from Employee import views as employee_views
urlpatterns = [
    path('employee', employee_views.employee_list),
    path('employee/<int:pk>/', employee_views.employee_detail),
]