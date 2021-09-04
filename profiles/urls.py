from django.urls import path
from . views import *

urlpatterns = [
    path('get_profile/<int:pk>',get_profile, name= 'get_profile'),
    path('user_profile/',user_profile, name= 'user_profile'),
    path('update_profile_image/',update_profile_image, name= 'update_profile_image'),
    path('update_profile/',update_profile, name= 'update_profile'),
    path('follow/',follow, name= 'follow'),
    path('unfollow/',unfollow, name= 'unfollow'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('prof_image/', prof_image, name='prof_image'),
]
