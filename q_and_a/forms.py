from django.db.models import fields
from django.forms import models
from q_and_a.models import Question, Answer
from django import forms
from froala_editor.widgets import FroalaEditor


class AskQusestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        
        fields = ['question_title','question','tags']

    def __init__(self, *args, **kwargs):
        super(AskQusestionForm, self).__init__(*args, **kwargs)
        self.fields['question_title'].widget.attrs['class'] = 'form-control'
        self.fields['question_title'].widget.attrs['placeholder'] = 'Title'
        self.fields['tags'].widget.attrs['class'] = 'form-control'


   
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description']

    # def __init__(self, *args, **kwargs):
    #     super(AnswerForm, self).__init__(*args, **kwargs)
    #     # self.fields['answer_title'].widget.attrs['class'] = 'form-control'
        
        
