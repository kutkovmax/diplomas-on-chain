from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ("username", "email", "password1", "password2")


class StudentLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
