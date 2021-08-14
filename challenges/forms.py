from django.db.models import fields
from .models import Challenge,ChallengeTopic
from django import forms


class challengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title','challenge_question','input_value','test_case','topic']

class ChallengeTopicForm(forms.ModelForm):
    class Meta:
        model = ChallengeTopic
        fields = ['title'] 