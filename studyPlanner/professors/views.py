from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from studyPlanner.core.models import Task, Class, User
from studyPlanner.students.models import Student_Exam
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
import datetime
from time import strftime, gmtime
from .forms import Student_ExamForm

# Create your views here.
def home(request):    
    context = {
        'nbar' : 'inicio'
     #   'tasks' : tasks
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

class Student_ExamCreate(CreateView):
    model = Student_Exam
    fields = ['student', 'examClass', 'gradeMod1', 'gradeMod2', 'gradeSub']
    template_name = 'professors/students.html'
    success_url = '/professors'

def turmas(request):
    turmas = Class.objects.all()
    for val in turmas:
        num = 0
        num = numAlunos(val.id)
        val.num = num.count()
    
    context = {
        'nbar' : 'turmas',
        'turmas' : turmas
        # 'grades' : grades
    }
    return render(request, 'professors/classes.html', context)

def alunos(request, id):
    # calcular as notas de cada módulo 
    # Módulo = (médias das entregas do aluno)*0.1 + (prova do módulo)*0.9
    # Média Final = médias dos módulos
    turma = Class.objects.get(id = id)
    alunos = Class.objects.filter(id = id).get().students.all()    
    for aluno in alunos:
        alunoNotas = Student_Exam.objects.filter(examClass_id = id, student_id=aluno.id).get()
        aluno.gradeMod1 = alunoNotas.gradeMod1
        aluno.gradeMod2 = alunoNotas.gradeMod2
        aluno.gradeSub = alunoNotas.gradeSub

    # if request.method == 'POST':
    #     grade_form = Student_ExamForm(request.POST, instance=request.user.person)
    #     if grade_form.is_valid():
    #         grade_form.save()
    #         context = {
    #             'message' : 'Notas alteradas com sucesso',
    #             'turma' : turma,
    #             'alunos' : alunos
    #         }
    #         return render(request, 'professors/students.html', context)
    #     else:
    #         print('It is not working')
    # else:
    #     grade_form = Student_ExamForm(instance=request.user.person)

    context = {
        'turma' : turma,
        'alunos' : alunos
        # 'grade_form' : grade_form        
    }
    return render(request, 'professors/students.html', context)    

def tarefas(request, id):
    turma = Class.objects.get(id = id)
    tarefas = Class.objects.filter(id = id).get().tasks.all()    
    
    context = {
        'turma' : turma,
        'tarefas' : tarefas
    }
    return render(request, 'professors/tasks.html', context)    

def getAverageCR():
    turmas = Class.objects.all()
    cr = 0.0
    avg = 0.0
    for t in turmas:
        alunos = Class.objects.filter(id = t.id).get().students.all()
        alunos.aggregate(avg = Avg('cr'))
        cr = cr + avg
    return (cr)
    
def turmaDetail(request, id):
    turma = Class.objects.get(id = id)
    alunos = Class.objects.filter(id = id).get().students.all()
    num = 0
    num = numAlunos(id)
    context = {
        'turma': turma,
        'alunos': alunos,
        'totalAlunos': num
    } 
    return render(request, 'professors/detalhe.html', context)

def numAlunos(id):
    alunos = Class.objects.filter(id = id).get().students
    return alunos

def entregas(request):
    turmas = Class.objects.all()
    #turmas = Class.objects.filter(idProfessor=profId)    
    for t in turmas:
        t.taskList = []
        t.taskList = Class.objects.filter(id = t.id).get().tasks.all()
    context = {
        'turmas': turmas,
        'nbar' : 'entregas'
        }
    return render(request, 'professors/entregas.html', context)

def add_grade(request):
    if request.method == 'POST':
        grade_form = Student_ExamForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            context = {
                'message' : 'Notas alteradas com sucesso'
            }
            return render(request, 'professors/students.html', context)
        else:
            print('It is not working')
    else:
        grade_form = Student_ExamForm(instance=request.user)
    
    context = {
        'grade_form' : grade_form
    }
    return render(request, 'core/user_form.html', context)

