from django.db import models
from froala_editor.fields import FroalaField

class ChallengeTopic(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Challenge(models.Model):
    title = models.CharField(max_length=25)
    challenge_question = FroalaField()
    input_value = models.CharField(max_length=25)
    test_case = models.CharField(max_length=25)
    topic = models.ForeignKey(ChallengeTopic, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
