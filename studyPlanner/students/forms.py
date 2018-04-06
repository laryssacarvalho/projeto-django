from django import forms
from .models import Student

class studentForm(forms.ModelForm):
    firstName = forms.CharField(label='Nome')
    lastName = forms.CharField(label='Sobrenome')
    username = forms.CharField(label='Usuário')    
    email = forms.EmailField(label='Email')
    class Meta:
        model = Student
        fields = ('firstName', 'lastName', 'username', 'email')
