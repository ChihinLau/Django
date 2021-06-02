from django.contrib import admin
from django.urls import path, include
#from .views import employee_list, employee_detail
from Talk_app import views as talk_views
urlpatterns = [
    path('', talk_views.talk_list),
    path('<int:pk>/', talk_views.talk_detail),
]