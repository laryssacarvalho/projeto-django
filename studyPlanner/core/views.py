from django.shortcuts import render
from django.contrib.auth import(authenticate,login)
from django.http import HttpResponse

from .forms import UserLoginForm
# Create your views here.

def index(request):
    return render(request, 'core/index-freelancer.html', {'nbar' : 'inicio'})

def login_view(request):
    title = "Login"
    print("joia")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        print("eai")
        ra = form.cleaned_data.get("ra")
        password = form.cleaned_data.get("password")

    return render(request,"login.html",{"form":form,"title":title})

def home_view(request):
    return render(request,"core/home.html")