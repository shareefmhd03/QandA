from typing import ContextManager
from blog.forms import BlogForm
from blog.models import Blog
from django.shortcuts import redirect, render

# Create your views here.
def view_blog(request):
    blog_exist = Blog.objects.filter(user = request.user).exists()
    blog = Blog.objects.filter(user = request.user)
    context= {
        'blog':blog,
        'blog_exist':blog_exist,
    }
    return render(request, 'user/blog.html',context)



def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                titl = form.cleaned_data['title']
                print(titl,'-------------------')
                desc = form.cleaned_data['description']
                image = form.cleaned_data['img']
                blog = Blog(title = titl, description = desc, img = image, user = request.user)
                blog.save()
                return redirect('view_blog')
    form = BlogForm()
    context= {
        'form': form
    }
    return render(request, 'user/blog_form.html',context)


    