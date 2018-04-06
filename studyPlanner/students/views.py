from django.shortcuts import render
from django.http import HttpResponse
from studyPlanner.core.models import Task
from .forms import studentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentUpdate(UpdateView):
    model = Student
    fields = ['firstName','lastName','email','ra']

def meuPerfil(request):
    if request.method == 'POST':
        form = studentForm(request.POST)        
    else:
        form = studentForm()
    return render(request, 'students/perfil.html', {'nbar' : 'perfil', 'form': form})

def agenda(request):
    return render(request, 'students/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    return render(request, 'students/notas.html', {'nbar' : 'notas'})

def entregas(request):
    tasks = Task.objects.all()
    context = {
        'nbar' : 'entregas',
        'tasks' : tasks
    }
    return render(request, 'students/entregas.html', context)

def home(request):
    return render(request, 'students/home.html', {'nbar' : 'inicio'})
    

