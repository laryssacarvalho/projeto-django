from django.urls import path
from .import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('meuPerfil', views.meuPerfil, name='meuPerfil'),
    #path('agenda', views.agenda, name='agenda'),
    path('turmas', views.turmas, name='turmas'),
    #path('editar/<int:pk>/', views.ProfessorUpdate.as_view(), name='professor_update'),
]