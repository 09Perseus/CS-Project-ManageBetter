from django.urls import path
from . import views

urlpatterns = [
     path("", views.tdefault, name="tdefault")
]