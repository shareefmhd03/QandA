from django.db.models import Count,Sum
from q_and_a.models import PointsTable
from profiles.models import Profile
from q_and_a.models import Question, Answer
from blog.models import Blog
from django.shortcuts import redirect, render

# Create your views here.

def user_profile(request):
    if request.user.is_authenticated:
        profile  = Profile.objects.get(user = request.user)
        question = Question.objects.filter(user = request.user)
        points = PointsTable.objects.get(user = request.user)
        blog = Blog.objects.filter(user = request.user)
        
        # owner = Accounts.objects.filter(id = 17)
        # print(owner)
    context ={
        'profile':profile,
        # 'points':points,
        'questions':question,
        'blogs':blog,
    }
    return render(request, 'user/user_profile.html', context)

def get_profile(request, pk):
    profile  = Profile.objects.get(id =pk)
    blog = Blog.objects.filter(user = profile.user)
    points = PointsTable.objects.get(user = profile.user)
    print(points.asked_questions_counter())
    # po = PointsTable.objects.annotate(num_quest = Count('asked_questions'))[0]
    # print(po.num_quest)
    # likes = PointsTable.objects.filter(user=profile.user).annotate(likes_count=Count('asked_questions'))
    # print(likes)

    # print(points.asked_questions_counter())
    context={
        'profile':profile,
        'blogs':blog,
    }
    return render(request, 'user/user_profile.html', context)

def update_profile_image(request):
    profile  = Profile.objects.get(user = request.user)
    if request.user.is_authenticated: 
        if request.method == "POST":
            image  = request.FILES['image_input']
            profile.profile_image =image
            profile.save()
        return redirect('user_profile')



def update_profile(request):
    pass
