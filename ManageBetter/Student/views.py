from django.shortcuts import render

# Create your views here.
def sdefault(request):
    return render(request, "Student/sdefault.html")