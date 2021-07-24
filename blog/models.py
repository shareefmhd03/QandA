from django.db import models
from accounts.models import Accounts

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    img  = models.ImageField(blank = True, upload_to = 'blog_images', null=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title