from blog.models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model  = Blog
        fields = ['title','img','description']