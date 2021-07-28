from blog.forms import BlogForm
from blog.models import Blog
from django.shortcuts import redirect, render

# Create your views here.
def view_blog(request):
    all_blogs = Blog.objects.all()
    
    context={
        'all_blogs':all_blogs,
    }
    try:
        blog_exist = Blog.objects.filter(user = request.user).exists()
        blog = Blog.objects.filter(user = request.user)
        context['blog']=  blog
        context['blog_exist'] = blog_exist
    except Exception as e:
        print(e)
    return render(request, 'user/blog.html',context)



def add_blog(request):
    context = {}
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = BlogForm(request.POST, request.FILES)
                if form.is_valid():
                    titl = form.cleaned_data['title']
                    desc = form.cleaned_data['description']
                    image = form.cleaned_data['img']
                    blog = Blog(title = titl, description = desc, img = image, user = request.user)
                    blog.save()
                    return redirect('view_blog')
            form = BlogForm()
            context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'user/blog_form.html',context)

def blog_detailed_view(request, slug):
    author = Blog.objects.filter(user = request.user, slug = slug).exists()

    context = {
        'author':author,
    }
    try:
        single_blog = Blog.objects.filter(slug = slug)
        context['single_blog'] = single_blog

    except Exception as e:
        print(e)
    return render(request, 'user/single_post.html', context)
        
 

def edit_blog(request, slug):
    context = {}
    blog = Blog.objects.get(slug = slug)
    form = BlogForm(instance=blog)
    solved = Blog.objects.filter(user = request.user, slug= slug).exists()
    if solved:

        if request.user.is_authenticated:
            if request.method == 'POST':
                form = Blog(request.POST, request.FILES, instance = blog)
               
                if form.is_valid():
                    titl = form.cleaned_data['title']
                    desc = form.cleaned_data['description']
                    image = form.cleaned_data['img']
                    blog.title = titl
                    blog.description = desc
                    blog.img  = image
                    blog.save()
                    return redirect('view_blog')
            
            context['form'] = form
    return render(request, 'user/blog_form.html',context)