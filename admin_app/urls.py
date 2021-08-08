from django.urls import path
from . import views

urlpatterns = [
    path('user_mgmt/',views.user_mgmt, name='user_mgmt'),
    path('add_user/',views.add_user, name='add_user'),
]