from tutorials.models import McqQuestions, Tutorial
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.


def tutorials(request):
    tutorial = Tutorial.objects.all()
    paginator = Paginator(tutorial, 6)
    page = request.GET.get('page')
    paged_tutorial = paginator.get_page(page)
    tutorial_count = tutorial.count()

    context = {
        'paged_tutorial': paged_tutorial,
        'tutorial_count': tutorial_count,
    }
    return render(request, 'user/tutorials.html', context)


def single_tutorial(request, slug):
    tutorial = Tutorial.objects.get(slug=slug)
    context = {
        'tutorial': tutorial
    }
    return render(request, 'user/single_tutorials.html', context)


def take_test(request, id):
    test = McqQuestions.objects.filter(topic_id=id)
    turorial = Tutorial.objects.get(id=id)
    context = {
        'test': test,
        'turorial': turorial,
    }
    return render(request, 'user/mcq.html', context)
