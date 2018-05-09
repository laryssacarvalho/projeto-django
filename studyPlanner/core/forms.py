from django.contrib.auth.models import User
from studyPlanner.core.models import Person
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('ra',)