from django.contrib.admin.sites import DefaultAdminSite, site
from django.db import models
from accounts.models import Accounts
from q_and_a.models import Question,Answer

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to ='profile',default = 'user.png')
    bio  = models.TextField(default='no bio..')
    following   = models.ManyToManyField(Accounts,related_name='following', blank=True)
    questions = models.ForeignKey(Question, models.DO_NOTHING, blank=True, null=True)
    answers =models.ForeignKey(Answer, models.DO_NOTHING, blank=True, null= True)
    # favorites
    # points
    # social links
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)