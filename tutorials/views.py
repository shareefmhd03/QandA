from tutorials.models import McqQuestions, Tutorial
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


def tutorials(request):
    tutorial = Tutorial.objects.all()
    # all_blogs = Blog.objects.all()[:4]
    paginator = Paginator(tutorial, 6)
    page = request.GET.get('page')
    paged_tutorial = paginator.get_page(page)
    tutorial_count = tutorial.count()
    
    context ={
        # 'tutorial':tutorial,
        'paged_tutorial':paged_tutorial,
        'tutorial_count':tutorial_count,

        # 'test':test,
    }
    return render(request, 'user/tutorials.html', context)

def single_tutorial(request, slug):
    tutorial = Tutorial.objects.get(slug =slug)
    # test = McqQuestions.objects.get(id = id)
    context = {
        'tutorial' : tutorial
    }
    return render(request, 'user/single_tutorials.html', context)


def take_test(request,id):
    test = McqQuestions.objects.filter(topic_id = id)
    context = {
        'test':test,
    }
    return render(request, 'user/mcq.html',context)