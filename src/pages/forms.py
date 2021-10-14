from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item
from django import forms

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required

    class Meta:
        model = User
        # is_staff for staff or not
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ItemForm(ModelForm):
    class Meta:
        model = Item

        fields = '__all__'
