from django import forms
from django.contrib.auth.models import User
from django.forms import fields

from .models import Accounts
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Accounts
        fields = ['email','first_name','last_name','phone']
