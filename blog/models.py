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
    slug = models.SlugField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Blog , self).save(*args, **kwargs)