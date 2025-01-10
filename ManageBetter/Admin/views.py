from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Schools, Admin, Student, Teacher, Classes, Grades



# Create your views here.

#Creating form for admin to login
class loginform(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

#This view will load the default webpage of the application
def default(request):
   
    if not request.user.is_authenticated:
        return userlogin(request)
    else:
        fname = request.user.first_name
        lname = request.user.last_name
        if request.user.role == "school_admin":
            details = Admin.objects.get(user=request.user)
            return render(request, "SAdmin/adminhomepage.html", {
                "fname":fname,
                "lname":lname,
                "school":details.schoolid.schoolname,
                "role":"School Admin"
            })
        elif request.user.role == "teacher":
            pass
        else:
            pass

#This view will load the login page if the request method is GET. Else it will log the user in and redirect them to their homepage
def userlogin(request):
    if request.method != "POST":
        #Return login page
        return render(request, "SAdmin/login.html", {
            "loginform": loginform()
        })
    else:
        #Get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "SAdmin/login.html", {
            "loginform": loginform(),
            "message": 'Invalid Username or Password'
            })
        else:
            login(request, user)
            if user.role == "school_admin":
                return HttpResponseRedirect(reverse("default"))
            elif user.role == "teacher":
                pass
            else:
                pass
            

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("default"))