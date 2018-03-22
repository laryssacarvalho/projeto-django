from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'students/home.html', {'nbar' : 'inicio'})

def meuPerfil(request):
    return render(request, 'students/perfil.html', {'nbar' : 'perfil'})

def agenda(request):
    return render(request, 'students/agenda.html', {'nbar' : 'agenda'})

def notas(request):
    return render(request, 'students/notas.html', {'nbar' : 'notas'})

def entregas(request):
    return render(request, 'students/entregas.html', {'nbar' : 'entregas'})

def login(request):
    return render(request, 'students/index-freelancer.html')