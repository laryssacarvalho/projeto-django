from django import forms
from .models import Professor

class professorForm(forms.ModelForm):
    firstName = forms.CharField(label='Nome')
    lastName = forms.CharField(label='Sobrenome')
    username = forms.CharField(label='Usuário')    
    email = forms.EmailField(label='Email')
    #tipo = forms.TypedChoiceField(choices=Professor.TIPOS, coerce=str) 
    class Meta:
        model = Professor
        fields = ('firstName', 'lastName', 'username', 'email')
        #fields = ('firstName', 'lastName', 'username', 'email','tipe')
