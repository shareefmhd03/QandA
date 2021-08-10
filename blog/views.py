from blog.forms import BlogForm, CommentForm
from blog.models import Blog, Comments, Reply
from django.shortcuts import redirect, render

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
    print('-------------------///////--------------')
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = BlogForm(request.POST, request.FILES)
                if form.is_valid():
                    print('111111111111///////--------------')
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
    form = CommentForm()
    single_blog = Blog.objects.get(slug = slug)
    comments = Comments.objects.filter(blog_id = single_blog)
    reply = Reply.objects.all()
    # if Blog.objects.filter(user = request.user, slug = slug).exists():
    #     author = True 
    # else:
    #     author = False
    context ={
        'form':form,
        # 'author':author,
        'comments':comments,
        'reply':reply,
        'single_blog':single_blog
    }
    return render(request, 'user/single_post.html', context)
        
 

def edit_blog(request, slug):
    context = {}
    blog = Blog.objects.get(slug = slug)
    form = BlogForm(instance=blog)
    blog_auther = Blog.objects.filter(user = request.user, slug= slug).exists()
    context['blog_auther'] = blog_auther
    if blog_auther:

        if request.user.is_authenticated:
            if request.method == 'POST':
                form = BlogForm(request.POST, request.FILES, instance = blog)
               
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



def my_blog(request):
    context ={}
    blog = Blog.objects.filter(user= request.user)
    context['blog'] = blog
    return render(request, 'user/my_blog.html', context)


def comment_section(request, slug):
    if request.user.is_authenticated:
        blog= Blog.objects.get(slug = slug)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid:
                comment = request.POST['comment']
                post_slug = request.POST['post_slug']
                Comments.objects.create(user = request.user, blog = blog, comment = comment)
                # blog_detailed_view(request, post_slu)
                return redirect('blog_detailed_view', slug)

def reply_section(request, pk, slug):
    if request.user.is_authenticated:
        reply = Comments.objects.get(id = pk)
        
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid:
                comment = request.POST['comment']
                Reply.objects.create(user = request.user, comment = comment, comment_name = reply)

                return redirect('blog_detailed_view', slug)



