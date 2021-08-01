from tutorials.models import Tutorial
from django.shortcuts import render

# Create your views here.


def tutorials(request):
    tutorial = Tutorial.objects.all()
    context ={
        'tutorial':tutorial,
    }
    return render(request, 'user/tutorials.html', context)

def single_tutorial(request, slug):
    tutorial = Tutorial.objects.get(slug =slug)
    context = {
        'tutorial' : tutorial
    }
    return render(request, 'user/single_tutorials.html', context)