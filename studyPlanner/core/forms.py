from django import forms

class UserLoginForm(forms.Form):
    ra = forms.CharField()
    email = forms.EmailField()