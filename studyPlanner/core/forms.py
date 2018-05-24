from django.contrib.auth.models import User
from studyPlanner.core.models import Person
from django.contrib.auth.forms import UserCreationForm
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('ra',)

class UserCreationForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField()

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
                    )
        return user

