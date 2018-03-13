from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'alunos/home.html', {'nbar' : 'inicio'})

def meuPerfil(request):
    return render(request, 'alunos/perfil.html', {'nbar' : 'perfil'})

def agenda(request):
    return render(request, 'alunos/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    return render(request, 'alunos/notas.html', {'nbar' : 'notas'})

def entregas(request):
    return render(request, 'alunos/entregas.html', {'nbar' : 'entregas'})

def login(request):
    return render(request, 'alunos/index-freelancer.html')