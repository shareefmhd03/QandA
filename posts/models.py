# from profiles.models import Profile
from django.db import models
from accounts.models import Accounts

# Create your models here.



class Posts(models.Model):
    image = models.ImageField(blank = True, upload_to = 'posts_images')
    description = models.TextField()
    # author = models.ForeignKey(Profile,on_delete=models.CASCADE, null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.pk)

    