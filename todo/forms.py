from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'completed', "user"]


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
