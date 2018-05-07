from django.shortcuts import render
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
import pyrebase

config = {
    'apiKey': "AIzaSyBBE__151mZb7-Dwm_YXlAgfVDhU2vcoUM",
    'authDomain': "study-planner-app.firebaseapp.com",
    'databaseURL': "https://study-planner-app.firebaseio.com",
    'projectId': "study-planner-app",
    'storageBucket': "study-planner-app.appspot.com",
    'messagingSenderId': "455361032393"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request,'login.html')

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    user = auth.sign_in_with_email_and_password(email,passw)
    # //print(user.email)
    return render(request,'core/welcome.html')
    # return render(request,'welcome.html',{"e":email})

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
