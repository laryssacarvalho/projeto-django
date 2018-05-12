from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from studyPlanner.core.models import Task, Class, User
from studyPlanner.students.models import Student_Exam, Task_Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
import datetime
from time import strftime, gmtime
from .forms import Student_ExamForm, Task_StudentForm

def home(request):    
    context = {
        'nbar' : 'inicio'
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
    for val in turmas:
        num = 0
        num = numAlunos(val.id)
        val.num = num.count()
    
    context = {
        'nbar' : 'turmas',
        'turmas' : turmas
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

    context = {
        'nbar' : 'turmas',        
        'turma' : turma,
        'alunos' : alunos
    }
    return render(request, 'professors/students.html', context)

def nota(request, idTurma, idAluno):
    turma = Class.objects.get(id = idTurma)
    try:
        alunoNotas = Student_Exam.objects.filter(examClass_id = idTurma, student_id=idAluno).get()    
    except Student_Exam.DoesNotExist:
        alunoNotas = False

    if request.method == 'POST':
        if alunoNotas:
            grade_form = Student_ExamForm(request.POST, instance=alunoNotas)
        else:
            grade_form = Student_ExamForm(request.POST)
            
        if grade_form.is_valid():
            grade_form.save()
            context = {
                'message' : 'Notas alteradas com sucesso',
                'grade_form' : grade_form,
                'turma' : turma
            }
            return render(request, 'professors/grade_form.html', context)
        else:
            print('It is not working')
    else:
        if alunoNotas:
            grade_form = Student_ExamForm(instance=alunoNotas)
        else:
            grade_form = Student_ExamForm()

    context = {
        'nbar' : 'turmas',
        'turma' : turma,
        'notas' : nota,
        'grade_form' : grade_form        
    }
    return render(request, 'professors/grade_form.html', context)

def nota_tarefa(request, id):
    try:
        tarefa = Task_Student.objects.get(id = id)        
    except Task_Student.DoesNotExist:
        tarefa = False

    if request.method == 'POST':
        grade_task_form = Task_StudentForm(request.POST, instance=tarefa)

        if grade_task_form.is_valid():
            grade_task_form.save()
            context = {
                'message' : 'Notas alteradas com sucesso',
                'grade_task_form' : grade_task_form
            }
            return render(request, 'professors/grade_task_form.html', context)
        else:
            print('It is not working')
    else:
        if tarefa:
            grade_task_form = Task_StudentForm(instance=tarefa)
        else:
            grade_task_form = Task_StudentForm()

    context = {
        'nbar' : 'turmas',
        'notas' : nota,
        'grade_task_form' : grade_task_form       
    }
    return render(request, 'professors/grade_task_form.html', context)  


def tarefas_aluno(request, idTurma, idAluno):    
    turma = Class.objects.get(id = idTurma)
    try:        
        tarefasAluno = Task_Student.objects.filter(task = idTurma, student = idAluno).all()
    except Task_Student.DoesNotExist:
        tarefasAluno = False
    
    context = {
        'nbar' : 'turmas',
        'turma' : turma,
        'tarefas' : tarefasAluno        
    }
    return render(request, 'professors/tasks_student.html', context)    

def alunos_tarefa(request, id):
    try:
        tarefas = Task_Student.objects.filter(task = id).all()
    except Task_Student.DoesNotExist:
        tarefas = False
    if tarefas:
        turma = tarefas[0].task.taskClass
    else:
        turma = False
    context = {
        'nbar' : 'turmas',
        'turma' : turma,
        'tarefas' : tarefas        
    }
    return render(request, 'professors/students_task.html', context)    

def tarefas(request, id):
    turma = Class.objects.get(id = id)
    tarefas = Class.objects.filter(id = id).get().tasks.all()    
    
    context = {
        'nbar' : 'turmas',                
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

def numAlunos(id):
    alunos = Class.objects.filter(id = id).get().students
    return alunos

