

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
    description = models.TextField()
    attachment = models.ImageField(upload_to='media', blank=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    is_solved =models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_title



class PointsTable(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    point = models.IntegerField()
    solved_questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    asked_questions  = models.ForeignKey(Answer, on_delete=models.CASCADE)


    