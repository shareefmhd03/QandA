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


class ChallengeQuestion(models.Model):
    qno = models.IntegerField(default=0)
    text = models.CharField(max_length=45000)
    test_case_no = models.IntegerField(default=0)
    sample_input = models.CharField(max_length=45000,default='')
    sample_output = models.CharField(max_length=45000,default='')
    test_case1 = models.CharField(max_length=1000)
    test_case2 = models.CharField(max_length=1000)
    test_case3 = models.CharField(max_length=1000)
    test_case1_sol = models.CharField(max_length=1010)
    test_case1_sol = models.CharField(max_length=1000)
    test_case3_sol = models.CharField(max_length=1000)
    def __str__(self):
        return self.text