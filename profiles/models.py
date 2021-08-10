from django.db import models
from accounts.models import Accounts
from q_and_a.models import  Question,Answer
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50, blank=True,null=True)
    profile_image = models.ImageField(upload_to ='profile', default = 'user.png')
    bio  = models.TextField(default='no bio..')
    following  = models.ManyToManyField(Accounts,related_name='following', blank=True)
    questions = models.ForeignKey(Question, on_delete = models.DO_NOTHING, blank=True, null=True)
    answers =models.ForeignKey(Answer, on_delete= models.DO_NOTHING, blank=True, null= True)

    # asked_questions = models.ManyToManyField(Question, blank = True, related_name='asked_question')
    # solved_questions = models.ManyToManyField(Answer, blank = True, related_name='solved_question')
    # favorites = models.ManyToManyField(Question,blank=True, null= True)
    # social links
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)



# @receiver(post_save, sender =Question)
# def asked_question_handler(sender, instance, created, *args, **kwargs):
#     if created:
#         print('question is created', instance.question_title)

