from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     
     path("login", views.userlogin, name="login"),
     path("logout", views.userlogout, name="logout"),
     path("manageteachers", views.manageteachers, name="manageteachers")
]