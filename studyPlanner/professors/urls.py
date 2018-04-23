from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name='home'),    
    path('meuPerfil', views.meuPerfil, name='meuPerfil'),
    path('agenda', views.agenda, name='agenda'),
    path('editar/<int:pk>/', views.ProfessorUpdate.as_view(), name='professor_update'),
    path('turmas', views.turmas, name='turmas'),
    path('', views.sair, name='sair'),

    path('turmas2', views.turmas2, name='turmas2'),
    path('detalhe/<int:id>/', views.turmaDetail, name='detalhe'),

]