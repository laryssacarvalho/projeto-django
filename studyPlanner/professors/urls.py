from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/agenda', views.agenda, name='agenda'),
    path('/tarefa', views.TaskCreate.as_view(), name='tarefa'),
    path('/nota/<int:idTurma>/<int:idAluno>', views.nota, name='nota'),
    path('/turmas', views.turmas, name='turmas'),
    path('/alunos/<int:id>/', views.alunos, name='alunos'),
    path('/tarefas/<int:id>/', views.tarefas, name='tarefas'),
    path('/tarefasAluno/<int:idTurma>/<int:idAluno>', views.tarefas_aluno, name='tarefasAluno'),
    path('/notaTarefa/<int:id>/', views.nota_tarefa, name='notaTarefa'),
    path('/alunosTarefa/<int:id>/', views.alunos_tarefa, name='alunosTarefa'),    
]