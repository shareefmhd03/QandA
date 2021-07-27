from q_and_a.models import Question, Answer
from django import forms
from froala_editor.widgets import FroalaEditor



class AskQusestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title','question','tags']



   
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_title', 'attachment','description']