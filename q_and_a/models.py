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
    upvote = models.ManyToManyField(Accounts, related_name='ques_likes')
    downvote = models.ManyToManyField(Accounts, related_name='ques_dislikes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.question_title)
        super(Question , self).save(*args, **kwargs)
    def upvote_count(self):
        return self.upvote.all().count()
    def downvote_count(self):
        return self.downvote.all().count()
    def vote_total(self):
        return self.upvote_count()-self.downvote_count()

class Answer(models.Model):
    # answer_title = models.CharField(max_length=200)
    user = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    description = FroalaField(theme='dark')
    
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True)
    upvote = models.ManyToManyField(Accounts, related_name='likes')
    downvote = models.ManyToManyField(Accounts, related_name='dislikes')
    tags = models.ManyToManyField(Tags)
    is_solution =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question.question_title

    def upvote_count(self):
        return self.upvote.all().count()
    def downvote_count(self):
        return self.downvote.all().count()

    def vote_total(self):
        return self.upvote_count()-self.downvote_count()

class PointsTable(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE, blank = True, null=True)
    point = models.IntegerField(blank = True, null=True, default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def upvote_count(self):
        return self.upvote.all().count()
    def downvote_count(self):
        return self.downvote.all().count()
    
    
