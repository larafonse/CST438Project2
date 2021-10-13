from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # is_staff for staff or not
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']