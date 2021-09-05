from django import forms
from django.db.models import fields
from .models import McqQuestions, Topics, Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['topics','title','About','Image','description','tutorials'] 

    def __init__(self, *args, **kwargs):
        super(TutorialForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs['class'] = 'form-control'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class TopicForm(forms.ModelForm):
    class Meta:
         model = Topics
         fields = ['tutorial_name','tut_image']
         
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        



class McQForm(forms.ModelForm):
    class Meta:
        model = McqQuestions
        fields = ['topic','question','option1','option2','option3','correct_answer']

    def __init__(self, *args, **kwargs):
        super(McQForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



