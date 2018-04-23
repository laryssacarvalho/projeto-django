from django.shortcuts import render
from django.http import HttpResponse
from .forms import professorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Professor
from studyPlanner.core.models import Class
from studyPlanner.core.models import User
from studyPlanner.core.models import Task

# Create your views here.

def meuPerfil(request):
    if request.method == 'POST':
        form = professorForm(request.POST)        
    else:
        form = professorForm()
    return render(request, 'professors/perfil.html', {'nbar' : 'perfil', 'form': form})

def agenda(request):
    return render(request, 'professors/agenda.html', {'nbar' : 'agenda'})

def home(request):
    return render(request, 'professors/home.html', {'nbar' : 'inicio'})

def turmas(request):
    return render(request, 'professors/turmas.html', {'nbar' : 'inicio'})

def sair(request):
    return render(request, 'professors/home.html', {'nbar' : 'inicio'})

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['firstName','lastName','email','ra','tipo']

# def turma_list(request):
#     turmas = Class.objects()
#     print(turmas)
#     return render(request, 'professors/turmas.html', {'nbar' : 'turmas'})

    
def turmas2(request):
    turmas = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)
    context = {
        'turmas': turmas
    } 
    return render(request, 'professors/turmas2.html', context)

def turmaDetail(request, id):
    turma = Class.objects.get(id = id)
    alunos = turma.idStudent.all()
    context = {
        'alunos': alunos
    } 
    return render(request, 'professors/detalhe.html', context)


def meuPerfil2(request):
    me = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)
    context = {
        'turmas': turmas
    } 
    return render(request, 'professors/turmas2.html', context)

def agenda2(request):
    agenda = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)
    context = {
        'turmas': turmas
    } 
    return render(request, 'professors/turmas2.html', context)