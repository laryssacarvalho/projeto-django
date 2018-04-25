from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task, Class
from .forms import studentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .models import Task_Student
from django.db import connection

class StudentUpdate(UpdateView):
    model = Student
    success_url="/alunos/"
    fields = ['firstName','lastName','email']

def agenda(request):
    return render(request, 'students/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    return render(request, 'students/notas.html', {'nbar' : 'notas'})

def entregas(request):
    context = {
        'nbar' : 'entregas'    
    }
    return render(request, 'students/entregas.html', context)

def home(request):
    #allTasks = Task.objects.filter(student_id=1).count()
    allTasks = len(list(Task.objects.raw('SELECT * FROM core_task')))
    
    
    student = Student.objects.filter(user_ptr_id=2)
    context = {
        'nbar' : 'inicio'
        #'cr' : student[0].cr
    }
    return render(request, 'students/home.html', context)
    
