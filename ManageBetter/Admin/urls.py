from django.urls import path
from . import views

urlpatterns = [
     path("", views.default, name="default"),
     path("login", views.userlogin, name="login"),
     path("logout", views.userlogout, name="logout")
]