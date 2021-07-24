from django.db.models import fields
from q_and_a.models import Question, Answer
from django import forms



class AskQusestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title','question','attachment']




class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_title', 'attachment', 'description', 'attachment']