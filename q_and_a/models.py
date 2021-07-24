from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import OneToOneField
from accounts.models import Accounts


# class Tags(models.Model):
#     tag_name = models.CharField(max_length=25)
#     tag_desc = models.TextField(blank=True)

#     def __str__(self):
#         return self.tag_name





class Question(models.Model):
    question_title  = models.CharField(max_length=200)
    user  = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    # tags =  models.ForeignKey(Tags, related_name='tag', on_delete=DO_NOTHING)
    attachment = models.ImageField(upload_to = 'media', blank = True)
    question = models.TextField()
    # answer = models.ForeignKey(Answer, blank = True, on_delete=DO_NOTHING, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    answer_title  = models.CharField(max_length=200)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    description = models.TextField()
    attachment = models.ImageField(upload_to = 'media', blank = True)
    # question = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_title


