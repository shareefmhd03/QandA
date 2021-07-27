from profiles.models import Profile
from django.shortcuts import render

# Create your views here.

def user_profile(request):

    context ={}
    try:
        if request.user.is_authenticated:
            profile  = Profile.objects.filter(user = request.user)

        context['profile'] = profile
        return render(request, 'user/user_profile.html', context)
    except:
        return render(request, 'user/login.html')