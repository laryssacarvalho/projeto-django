from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task, Class, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task_Student, Student_Exam
from django.db import connection
from datetime import date, datetime
import calendar
from django.contrib.auth.models import User
from studyPlanner.students.models import Student_Exam, Task_Student, Task


def agenda(request):   
    today = datetime.today()
    tarefas = Task.objects.all()

    context = {
        'nbar' : 'agenda',
        'month': calendar.month_name[today.month],
        'year': today.year,
        'tarefas' : tarefas      
    }
    return render(request, 'students/agenda.html', context)

def notas(request):
    classes = Task.objects.filter().all()
    context = {
        'nbar' : 'notas'
        # 'grades' : grades
    }
    return render(request, 'students/notas.html', context)

def entregas(request):   
    tlist = Class.objects.get().tasks.all()       
    context = {
        'tarefas': tlist
    }
    return render(request, 'students/entregas.html', context)

def numAlunos(id):
    alunos = Class.objects.filter(id = id).get().students
    return alunos

def home(request):

    name = request.user
    id = request.user.id
    tarefas = Task.objects.all()
    tasks = len(tarefas)
    aulas = Class.objects.all()
    classes = len(aulas)
    today = datetime.today()

    context = {
        'nbar' : 'inicio',
        'name' : name,
        'tarefas': tarefas,
        'tasks': tasks,
        'classes': classes,
        'id': id,
        'month': calendar.month_name[today.month]
    }
    return render(request, 'students/home.html', context)
    
