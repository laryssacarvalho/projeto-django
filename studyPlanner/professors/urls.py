from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/agenda', views.agenda, name='agenda'),
    path('/tarefa', views.TaskCreate.as_view(), name='tarefa'),
    path('/turmas', views.turmas, name='turmas')
]