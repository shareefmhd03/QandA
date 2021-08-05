from profiles.models import Profile
from django.shortcuts import redirect, render

# Create your views here.

def user_profile(request):

  
    if request.user.is_authenticated:
        profile  = Profile.objects.get(user = request.user)
        # print(profile.profile_image)

    context ={
        'profile':profile,
    }
    
    return render(request, 'user/user_profile.html', context)

def update_profile_image(request):
    profile  = Profile.objects.get(user = request.user)
    
    if request.user.is_authenticated:
        if request.method == "POST":
            image  = request.FILES['image_input']
            profile.profile_image =image
            profile.save()
    return redirect('user_profile', )
