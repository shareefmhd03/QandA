from django.db import models
from froala_editor.fields import FroalaField
from accounts.models import Accounts


class ChallengeTopic(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# class Challenge(models.Model):
#     title = models.CharField(max_length=25)
#     challenge_question = FroalaField()
#     input_value = models.CharField(max_length=25)
#     test_case = models.CharField(max_length=25)
    

#     def __str__(self):
#         return self.title


class ChallengeQuestion(models.Model):
    # user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    topic = models.ForeignKey(ChallengeTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=45000)
    desc = models.TextField(blank=True,null=True)
    challenge_question = FroalaField()

    sample_input = models.CharField(max_length=45000,default='',blank=True, null=True)
    sample_output = models.CharField(max_length=45000,default='', blank=True, null=True)
    test_case1 = models.CharField(max_length=1000, blank=True, null=True)
    test_case1_sol = models.CharField(max_length=1010, blank=True, null=True)

    def __str__(self):
        return self.title


class SolvedQuestion(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    challenges= models.ManyToManyField(ChallengeQuestion, related_name="solved_challenges")

    def __str__(self):
        return self.user