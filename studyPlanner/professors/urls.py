from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/agenda', views.agenda, name='agenda'),
    path('/tarefa', views.TaskCreate.as_view(), name='tarefa'),
    path('/nota', views.Student_ExamCreate.as_view(), name='nota'),
    path('/turmas', views.turmas, name='turmas'),
    path('/alunos/<int:id>/', views.alunos, name='alunos'),
    path('/tarefas/<int:id>/', views.tarefas, name='tarefas')
]