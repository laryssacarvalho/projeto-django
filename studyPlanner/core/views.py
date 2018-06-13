from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .forms import UserForm, PersonForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# def index(request):
#     return render(request, 'core/index-agency.html', {'nbar' : 'inicio'})

@login_required
def home(request):
    if request.user.person.tipo == 'S':
        red = '/alunos'
    else:
        red = '/professors'    
    return redirect(red)

def user_profile(request):
    if request.user.person.tipo == 'S':
        header = 'students/header.html'
    else:
        header = 'professors/header.html'
    context = {
                'header' : header
            }
    return render(request, 'core/user_profile.html',context)

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
    
