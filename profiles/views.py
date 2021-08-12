from django.db.models import Count,Sum
from q_and_a.models import PointsTable
from profiles.models import Profile
from q_and_a.models import Question, Answer
from blog.models import Blog
from django.shortcuts import redirect, render



def user_profile(request):
    if request.user.is_authenticated:
        profile  = Profile.objects.get(user = request.user)
        question = Question.objects.filter(user = request.user)
        my_points = PointsTable.objects.get(user = request.user)
        followers = profile.following.all().count()
        
        blog = Blog.objects.filter(user = request.user)
        questions_count = Question.objects.filter(user = profile.user).count()

        
        # owner = Accounts.objects.filter(id = 17)
        # print(owner)
    context ={
        'profile':profile,
        'my_points':my_points,
        'followers':followers,
        'questions':question,
        'blogs':blog,
        'questions_count':questions_count,
    }
    return render(request, 'user/user_profile.html', context)

def get_profile(request, pk):
    followed = False
    profile  = Profile.objects.get(id =pk)
    blog = Blog.objects.filter(user = profile.user).order_by('created_at')
    points = PointsTable.objects.get(user = profile.user)
    followers = profile.following.all().count()
    
    questions = Question.objects.filter(user = profile.user)
    questions_count = Question.objects.filter(user = profile.user).count()
    if request.method =='POST':
        print('inside_post')
        if request.user in profile.following.all():
            followed = True

        if followed:
            profile.following.remove(request.user)
            profile.save()
        else:
            profile.following.add(request.user)
            profile.save()
    
    # print(profile.following.use,'eeeee')
    print(followed)

    context={
        'profile':profile,
        'followers':followers,
        'blogs':blog,
        'questions':questions,
        'questions_count':questions_count,
        'followed':followed,
        'my_points':points,
        

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
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user)
        if request.method =="POST":
            bio = request.POST['bio']
            designation = request.POST['designation']

            profile.bio=bio
            profile.designation= designation
            profile.save()
            return redirect('user_profile')

def follow(request):
    if request.method == 'POST':
        val = request.POST['data']
        profile = Profile.objects.get(id = val)
        profile.following.add(profile.user)
        profile.save()
    return redirect('user_profile')