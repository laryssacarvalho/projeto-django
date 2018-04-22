from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task
from .forms import professorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Professor

# Create your views here.

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['firstName','lastName','email','ra','tipo']

def meuPerfil(request):
    if request.method == 'POST':
        form = studentForm(request.POST)        
    else:
        form = studentForm()
    return render(request, 'professors/perfil.html', {'nbar' : 'perfil', 'form': form})

def agenda(request):
    return render(request, 'professors/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    return render(request, 'professors/notas.html', {'nbar' : 'notas'})

def home(request):
    return render(request, 'professors/home.html', {'nbar' : 'inicio'})

def turmas(request):
    return render(request, 'professors/turmas.html', {'nbar' : 'turmas'})