from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from studyPlanner.core.models import Task, Class, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
import datetime
from time import strftime, gmtime

# Create your views here.
def home(request):
    #tasks = Task.objects.filter.all().count()
    context = {
        'nbar' : 'inicio'
     #   'tasks' : tasks
    }
    return render(request, 'professors/home.html', context)

def agenda(request):    
    context = {
        'nbar' : 'agenda',
        'month' : strftime("%B",gmtime()),
        'year' : strftime("%Y",gmtime())
    }
    return render(request, 'professors/agenda.html', context)

class TaskCreate(CreateView):
    model = Task
    fields = ['idTaskType', 'date', 'name', 'file', 'taskClass']
    template_name = 'professors/task_form.html'
    success_url = '/professors'

def turmas(request):
    turmas = Class.objects.all()
    for val in turmas:
        num = 0
        num = numAlunos(val.id)
        val.num = num.count()
    
    context = {
        'nbar' : 'turmas',
        'turmas' : turmas
        # 'grades' : grades
    }
    return render(request, 'professors/classes.html', context)

def alunos(request, id):
    turma = Class.objects.get(id = id)
    alunos = Class.objects.filter(id = id).get().students.all()    
    context = {
        'turma' : turma,
        'alunos' : alunos
    }
    return render(request, 'professors/students.html', context)    

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
    return alunos

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
