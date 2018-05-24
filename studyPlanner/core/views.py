from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib import auth
import pyrebase

config = {
    'apiKey': "AIzaSyBBE__151mZb7-Dwm_YXlAgfVDhU2vcoUM",
    'authDomain': "study-planner-app.firebaseapp.com",
    'databaseURL': "https://study-planner-app.firebaseio.com",
    'projectId': "study-planner-app",
    'storageBucket': "study-planner-app.appspot.com",
    'messagingSenderId': "455361032393"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

def signIn(request):
    return render(request,'login.html')


def createUser(request):
    print('deu certo')
    return render(request,'core/home.html')

def register(request):
    return render(request,'core/register.html')

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        us = authe.sign_in_with_email_and_password(email,passw)
        session_id = us['idToken']
        request.session['uid']=str(session_id)
        return render(request,'students/home.html',{"e":email})
    except:
        message = "Credenciais Inválidas."
        return render(request,'core/login.html',{"msg":message})

def logout(request):
    auth.logout(request)
    return render(request,"core/login.html")
from .forms import UserForm, PersonForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# def index(request):
#     return render(request, 'core/index-agency.html', {'nbar' : 'inicio'})

@login_required
def home(request):
    return render(request,'core/home.html')
    if request.user.person.tipo == 'S':
        red = '/alunos/'
    else:
        red = '/professors'    
    return redirect(red)

def user_profile(request):
    return render(request, 'core/user_profile.html')

def create_profile(request):
    if request.user.person.tipo == 'S':
        header = 'students/header.html'
    else:
        header = 'professors/header.html'
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():            
            user_form.save()
            context = {
                'header' : header,
                'user_form' : user_form,
                'message' : 'Perfil editado com sucesso!',
                'nbar' : 'perfil'
            }
            return render(request, 'core/user_form.html', context)
        else:
            print('It is not working')
    else:
        user_form = UserForm(instance=request.user)
    context = {
        'header' : header,
        'user_form' : user_form,
        'nbar' : 'perfil'
    }
    
    return render(request, 'core/user_form.html', context)
    
