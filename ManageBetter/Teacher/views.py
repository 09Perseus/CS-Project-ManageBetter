from django.shortcuts import render

# Create your views here.
def tdefault(request):
    return render(request, "Teacher/tdefault.html")