from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('meuPerfil', views.meuPerfil, name='meuPerfil'),
    path('agenda', views.agenda, name='agenda'),
    path('notas', views.notas, name='notas'),
    path('entregas', views.entregas, name='entregas'),
    path('editar/<int:pk>/', views.StudentUpdate.as_view(), name='student_update'),

]