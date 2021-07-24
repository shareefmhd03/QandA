from profiles.models import Profile
from django.shortcuts import render

# Create your views here.

def user_profile(request):
    profile  = Profile.objects.filter(user = request.user)

    context = {
        'profile':profile
    }
    return render(request, 'user/user_profile.html', context)