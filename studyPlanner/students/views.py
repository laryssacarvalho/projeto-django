from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task, Class, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .models import Task_Student, Student_Exam
from django.db import connection

def agenda(request):
    return render(request, 'students/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    classes = Task.objects.filter().all()
    context = {
        'nbar' : 'notas',
        'grades' : grades
    }
    return render(request, 'students/notas.html', context)

def entregas(request):
    context = {
        'nbar' : 'entregas'    
    }
    return render(request, 'students/entregas.html', context)

def home(request):
    #allTasks = Task.objects.filter(student_id=1).count()
    #allTasks = Student.objects.filter(id=2)
    allTasks = len(list(Task.objects.raw('SELECT * FROM core_task')))    
    student = Student.objects.filter(user_ptr_id=2).get()
    context = {
        'nbar' : 'inicio',
        'cr' : student.cr
    }
    return render(request, 'students/home.html', context)
    
