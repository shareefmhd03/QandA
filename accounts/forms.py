from .models import Accounts
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = Accounts
        fields = ['email','first_name','last_name','phone']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'