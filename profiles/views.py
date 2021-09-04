from django.db.models import Count,Sum
from django.db.models.query_utils import Q
from q_and_a.models import PointsTable
from profiles.models import Profile
from q_and_a.models import Question, Answer
from blog.models import Blog
from django.shortcuts import redirect, render
from chat.models import Thread



def user_profile(request):
    thread = False
    if request.user.is_authenticated:
        profile  = Profile.objects.get(user = request.user)
        question = Question.objects.filter(user = request.user)
        my_points = PointsTable.objects.get(user = request.user)
        followers = profile.following.all().count()        
        blog = Blog.objects.filter(user = request.user)
        questions_count = Question.objects.filter(user = profile.user).count()

        if Thread.objects.filter(Q(first_person=request.user) | Q(second_person=request.user)).exists():
            thread = True



    context ={
        'profile':profile,
        'my_points':my_points,
        'followers':followers,
        'questions':question,
        'blogs':blog,
        'thread':thread,

        'questions_count':questions_count,
    }
    return render(request, 'user/user_profile.html', context)



def prof_image(request):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user = request.user)
    context = {
        'profile' : profile,
    }
    return render(request,'user/includes/profile_image.html',context)

def get_profile(request, pk):
    followed = False
    profile  = Profile.objects.get(id =pk)
    user_profile  = Profile.objects.get(user =request.user)
    blog = Blog.objects.filter(user = profile.user).order_by('created_at')
    points = PointsTable.objects.get(user = profile.user)
    followers_count = profile.following.all().count()
    

    followers = user_profile.following.all()
    

    questions = Question.objects.filter(user_id = profile.user)
    print(questions)
    questions_count = Question.objects.filter(user = profile.user).count()


    if profile.user in followers:
        followed = True

           
        # else:
        #     profile.following.add(request.user)
        #     profile.save()
            # if Thread.objects.filter(Q(first_person=request.user,second_person=profile.user) | Q(first_person=profile.user,second_person=request.user)).exists():

            #     print('hello')
            # else:
            #     thread_obj=Thread(first_person=request.user,second_person=profile.user)
            #     thread_obj.save()
    context={
            'profile'        :profile,
            'followers'      :followers_count,
            'blogs'          : blog,
            'questions'      : questions,
            'questions_count':questions_count,
            'followed'       :followed,
            'my_points'      :points, 
        }
    return render(request, 'user/user_profile.html', context)



def follow(request):
    val = request.POST['data']
    profile  = Profile.objects.get(id =val)
    user_profile  = Profile.objects.get(user =request.user)

    user_profile.following.add(profile.user)
    user_profile.save()

    if Thread.objects.filter(Q(first_person=request.user,second_person=profile.user) | Q(first_person=profile.user,second_person=request.user)).exists():
        print('thread already exist!!!')
    else:
        thread_obj=Thread(first_person=request.user,second_person=profile.user)
        thread_obj.save()
    return redirect('get_profile', val)


def unfollow(request):
    val = request.POST['data']
    profile  = Profile.objects.get(id =val)
    user_profile  = Profile.objects.get(user =request.user)
    user_profile.following.remove(profile.user)
    user_profile.save()
    print('sdfgsdfgdsfff--------------')
    return redirect('get_profile', val)


def update_profile_image(request):
    profile  = Profile.objects.get(user = request.user)
    if request.user.is_authenticated: 
        if request.method == "POST":
            image  = request.FILES['image_input']
            profile.profile_image =image
            profile.save()
        return redirect('user_profile')



def update_profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user)
        if request.method =="POST":
            bio = request.POST['bio']
            designation = request.POST['designation']

            profile.bio=bio
            profile.designation= designation
            profile.save()
            return redirect('user_profile')

# def follow(request):
#     if request.method == 'POST':
#         
#         profile = Profile.objects.get(id = val)
#         profile.following.add(profile.user)
#         profile.save()
#     return redirect('user_profile')


def leaderboard(request):
    p =Profile.objects.order_by("-n_subm")
    users = {"user":p}
    return render(request,"user/leaderboard.html",users)