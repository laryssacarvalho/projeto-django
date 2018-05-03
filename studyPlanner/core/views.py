from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

def index(request):
    return render(request, 'core/index-agency.html', {'nbar' : 'inicio'})    

class UserUpdate(UpdateView):
    model = User
    success_url="/alunos/"
    fields = ['firstName','lastName','email']
    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)        
        try:
            user = User.objects.filter(id=self.kwargs['pk']).get().student 
            header = "students/header.html"                           
        except ObjectDoesNotExist:
            header = "professors/header.html"            
        context['header'] = header
        return context

def home(request):
    return render(request,'core/home.html')