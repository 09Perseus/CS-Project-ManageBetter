from django.urls import path
from . import views

urlpatterns = [
     path("", views.default, name="default"),
     path("adminlogin", views.adminlogin, name="adminlogin")
]