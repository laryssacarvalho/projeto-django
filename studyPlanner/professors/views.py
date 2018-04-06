from django.shortcuts import render

# Create your views here.

def turmas(request):
    return render(request, 'professors/turmas.html', {'nbar' : 'turmas'})