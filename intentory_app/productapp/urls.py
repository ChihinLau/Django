from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name="product-home"),
    path("about/", views.about, name="product-about"),
]
