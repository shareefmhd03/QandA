

from django.db import models
from accounts.models import Accounts
from froala_editor.fields import FroalaField

class Tags(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    question = FroalaField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    answer_title = models.CharField(max_length=200)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    description = FroalaField()
    
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    is_solved =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_title

class PointsTable(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE, blank = True, null=True)
    point = models.IntegerField(blank = True, null=True)
    solved_questions = models.ManyToManyField(Question, blank = True)
    asked_questions  = models.ManyToManyField(Answer, blank = True)

    def __str__(self):
        return self.user.username
