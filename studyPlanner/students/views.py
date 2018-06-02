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

# def agenda(request):
#     return render(request, 'students/agenda.html', {'nbar' : 'agenda'})

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
    context = {
        'nbar' : 'entregas'    
    }
    return render(request, 'students/entregas.html', context)

def home(request):
    context = {
        'nbar' : 'inicio'
        #'cr' : User.
    }
    return render(request, 'students/home.html', context)
    
