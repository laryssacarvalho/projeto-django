from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task, Class, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
import datetime
from time import strftime, gmtime

# Create your views here.
def home(request):
    tasks = Task.objects.filter.all().count()
    context = {
        'nbar' : 'inicio',
        'tasks' : tasks
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
    # classes = Task.objects.filter().all()
    context = {
        'nbar' : 'turmas',
        'turmas' : turmas
        # 'grades' : grades
    }
    return render(request, 'professors/classes.html', context)