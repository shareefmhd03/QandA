from functools import total_ordering
from django.db import models

from accounts.models import Accounts
from froala_editor import views
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from .slug_helper import slug_generator

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    img  = models.ImageField(blank = True, upload_to = 'blog_images', null=True)
    title = models.CharField(max_length=250, blank=True, null = True)
    description = FroalaField(blank= True, null = True)
    slug = models.SlugField(max_length=1000, blank=True, null=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Blog , self).save(*args, **kwargs)

class Comments(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.comment


class Reply(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    comment_name = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(max_length= 255 , blank= True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
