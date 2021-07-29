from blog.models import Blog, Comments
from django import forms
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
    class Meta:
        model  = Blog
        fields = ['title','description','img']


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Blog Title..'
        self.fields['img'].help_text = None


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comments
        fields = ['comment']
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['class'] = 'form-control'

