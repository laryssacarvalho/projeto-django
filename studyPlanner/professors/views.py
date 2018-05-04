from django.shortcuts import render
from django.http import HttpResponse
from .forms import professorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Professor
from studyPlanner.core.models import Class
from studyPlanner.core.models import User
from studyPlanner.core.models import Task
from django.db.models import Avg


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
    id = 1 #professorId
    context = {
        'cr': 0.0,
    } 
    #return render(request, 'professors/home.html', {'nbar' : 'inicio'})
    return render(request, 'professors/home.html', {'nbar' : 'inicio'}, context)

def getAverageCR(id):
    #turmas = Class.objects.filter(idProfessor=profId)
    #alunos = turmas.objects.filter(id = id).get().students
    turmas = Class.objects.all()
    cr = 0.0
    avg = 0.0
    for t in turmas:
        alunos = Class.objects.filter(id = t.id).get().students.all()
        alunos.aggregate(avg = Avg('cr'))
        cr = cr + avg
        #for al in t:
            #alunos = Class.objects.filter(id = al.id).sum().students.cr.all()
            #cr += sum(alunos.cr)/len(alunos)
    return (cr)

def sair(request):
    return render(request, 'professors/home.html', {'nbar' : 'inicio'})

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['firstName','lastName','email','ra','tipo']
    
def turmas(request):
    turmas = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)
    for val in turmas:
        num = 0
        num = numAlunos(val.id)
        val.num = num

    context = {
        'turmas': turmas
    } 
    return render(request, 'professors/turmas.html', context)

def turmaDetail(request, id):
    turma = Class.objects.get(id = id)
    alunos = Class.objects.filter(id = id).get().students.all()
    num = 0
    num = numAlunos(id)
    context = {
        'turma': turma,
        'alunos': alunos,
        'totalAlunos': num
    } 
    return render(request, 'professors/detalhe.html', context)

def numAlunos(id):
    alunos = Class.objects.filter(id = id).get().students
    return alunos.count()

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

def entregas(request):
    turmas = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)    
    for t in turmas:
        t.taskList = []
        t.taskList = Class.objects.filter(id = t.id).get().tasks.all()
    context = {
        'turmas': turmas,
        'nbar' : 'entregas'
        }
    return render(request, 'professors/entregas.html', context)
