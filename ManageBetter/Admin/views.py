from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms


# Create your views here.

#This view will load the default webpage of the application
def default(request):
    return render(request, "Admin/default.html")

#Creating form for admin to login
class adminloginform(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

#This view will load the admin login page if the request method is GET. Else it will log the user in and redirect them to their homepage
def adminlogin(request):
    if request.method != "POST":
        #Return login page
        return render(request, "Admin/adminlogin.html", {
            "adminloginform": adminloginform()
        })
    else:
        #Get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "Admin/adminlogin.html", {
            "adminloginform": adminloginform(),
            "message": 'Invalid Username or Password'
            })
        else:
            login(request, user)
            return render(request, "Admin/adminhomepage.html")
