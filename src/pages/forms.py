from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # is_staff for staff or not
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ItemForm(ModelForm):
    class Meta:
        model = Item

        fields = '__all__'