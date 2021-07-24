from django.contrib.admin.sites import DefaultAdminSite, site
from django.db import models
from accounts.models import Accounts

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = 'profile',default = 'user.png')
    bio  = models.TextField(default='no bio..')
    # questions
    # answers
    # favorites
    # points
    # social links
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
