from blog.models import Blog
from django import forms
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
    class Meta:
        model  = Blog
        fields = ['title','description','img']