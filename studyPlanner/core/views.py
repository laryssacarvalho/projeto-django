from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .forms import UserForm, PersonForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index-agency.html', {'nbar' : 'inicio'})

@login_required
def home(request):
    if request.user.person.tipo == 'A':
        redirect = '/alunos/'
    else:
        redirect = '/professors/'    
    return HttpResponseRedirect(
        reverse(home, args=[request.user]))

def user_profile(request):
    return render(request, 'core/user_profile.html')

def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        person_form = PersonForm(request.POST, instance=request.user.person)
        if user_form.is_valid() and person_form.is_valid():
            user_form.save()
            person_form.save()
            return render(request, 'core/user_profile.html', {})
        else:
            print('It is not working')
    else:
        user_form = UserForm(instance=request.user)
        person_form = PersonForm(instance=request.user.person)
    if request.user.person.tipo == 'S':
        header = 'students/header.html'
    else:
        header = 'professors/header.html'
    context = {
        'header' : header,
        'user_form' : user_form,
        'person_form' : person_form
    }
    return render(request, 'core/user_form.html', context)
    
