from django import forms
from .models import Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title','About','Image','description','Tutorial'] 

    def __init__(self, *args, **kwargs):
        super(TutorialForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs['class'] = 'form-control'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

