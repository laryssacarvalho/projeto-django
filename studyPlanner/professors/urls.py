from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/agenda', views.agenda, name='agenda'),
    path('/tarefa', views.TaskCreate.as_view(), name='tarefa'),
    path('/turmas', views.turmas, name='turmas'),
    path('/alunos/<int:id>/', views.alunos, name='alunos')
    # path('professors', views.home, name='home'), 
    # path('Home', views.home, name='Home'),    
    # path('MeuPerfil', views.meuPerfil, name='MeuPerfil'),
    # path('Agenda', views.agenda, name='Agenda'),
    # path('Editar/<int:pk>/', views.ProfessorUpdate.as_view(), name='professor_update'),
    # path('Turmas', views.turmas, name='Turmas'),
    # path('Entregas', views.entregas, name='Entregas'),
    # path('', views.sair, name='sair'),
    # path('detalhe/<int:id>/', views.turmaDetail, name='detalhe')
]