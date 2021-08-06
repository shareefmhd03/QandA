
from q_and_a.slug_helper import slug_generator
from django.db import models
from django.db.models.fields import SlugField
from accounts.models import Accounts
from froala_editor.fields import FroalaField


class Tags(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    slug = SlugField(max_length=250)
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    
    question = FroalaField()
    tags = models.ManyToManyField(Tags)
    solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.question_title)
        super(Question , self).save(*args, **kwargs)

class Answer(models.Model):
    # answer_title = models.CharField(max_length=200)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    description = FroalaField()
    
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    is_solution =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

class PointsTable(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE, blank = True, null=True)
    point = models.IntegerField(blank = True, null=True, default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def solved_ans_count(self):
        return self.solved_questions.all().count()

    def asked_questions_counter(self):
        return self.asked_questions.all().count()

        
    def upvote_count(self):
        return self.upvote
    
    def down_vote(self):
        return self.downvote

