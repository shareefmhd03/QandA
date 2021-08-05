from django.urls import path
from .views import *

urlpatterns = [
    path('user_profile/',user_profile, name= 'user_profile'),
    path('update_profile_image/',update_profile_image, name= 'update_profile_image'),
]