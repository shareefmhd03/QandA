from django.db import models
from froala_editor.fields import FroalaField
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from .slug_helper import slug_generator



class Tutorial(models.Model):
    title  = models.CharField(max_length=50)
    
    # turorial  = RichTextUploadingField()
    description  = FroalaField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Tutorial , self).save(*args, **kwargs)


class Topics(models.Model):
    tutorial = models.OneToOneField(Tutorial, on_delete=models.CASCADE)
    tut_image = models.ImageField(blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    