from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Schools, Admin, Student, Teacher, Classes, Grades



# Create your views here.

#This view will load the default webpage of the application
def default(request):
    """
    if request.user.is_authenticated == False:
        return userlogin(request)
    else:
        fname = request.user.first_name
        lname = request.user.last_name

        return render(request, "Admin/adminhomepage.html", {
            "fname":fname,
            "lname":lname
        })
    """
    #Return login page
    return render(request, "Admin/login.html", {
        "adminloginform": adminloginform()
    })

#Creating form for admin to login
class adminloginform(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())


#This view will load the login page if the request method is GET. Else it will log the user in and redirect them to their homepage
def userlogin(request):
    if request.method != "POST":
        #Return login page
        return render(request, "Admin/login.html", {
            "adminloginform": adminloginform()
        })
    else:
        #Get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "Admin/login.html", {
            "adminloginform": adminloginform(),
            "message": 'Invalid Username or Password'
            })
        else:
            login(request, user)
            if user.role == "School Admin":
                return HttpResponseRedirect(reverse("default"))
            elif user.role == "Teacher":
                pass
            elif user.role == "Student":
                pass

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("default"))