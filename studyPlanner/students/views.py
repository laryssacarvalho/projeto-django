from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task, Class, User, Person
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
    id = request.user.id
    turmas = User.objects.filter(id = id).get().person.classes_student.all()
    for turma in turmas:
        entregas = turma.tasks.all()
        turma.entregas = entregas
    

    
    context = {
        'nbar' : 'entregas',
        'turmas' : turmas
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
    
