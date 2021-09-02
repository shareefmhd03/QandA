from django.db.models import fields
from .models import ChallengeQuestion,ChallengeTopic
from django import forms


class challengeForm(forms.ModelForm):
    class Meta:
        model = ChallengeQuestion
        fields = ['topic','title','desc','challenge_question','sample_input','sample_output','test_case1','test_case1_sol']

    def __init__(self, *args, **kwargs):
        super(challengeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
class ChallengeTopicForm(forms.ModelForm):
    class Meta:
        model = ChallengeTopic
        fields = ['title','description','image'] 

    def __init__(self, *args, **kwargs):
        super(ChallengeTopicForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'