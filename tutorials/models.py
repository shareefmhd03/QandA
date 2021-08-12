from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from froala_editor.fields import FroalaField
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from .slug_helper import slug_generator


class Topics(models.Model):
    tutorial_name = models.CharField(max_length=50)
    tut_image = models.ImageField(blank = True, null = True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tutorial_name


class Tutorial(models.Model):
    title  = models.CharField(max_length=50)
    About = models.CharField(blank=True, null=True, max_length=300)
    Image= models.ImageField(null = True, blank = True, upload_to = 'tutorials')
    description = models.TextField(blank=True,null=True)
    tutorials  = FroalaField()
    slug = models.SlugField()
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Tutorial , self).save(*args, **kwargs)

class McqQuestions(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    question = models.CharField(max_length=300,blank=True, null=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question