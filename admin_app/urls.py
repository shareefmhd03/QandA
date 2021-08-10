from django.urls import path
from . import views

urlpatterns = [
    path('user_mgmt/',views.user_mgmt, name='user_mgmt'),
    path('add_user/',views.add_user, name='add_user'),
    path('user_unblock/',views.user_unblock, name='user_unblock'),
    path('delete_user/',views.delete_user, name='delete_user'),
    path('view_tutorials/',views.view_tutorials, name='view_tutorials'),
    path('add_tutorials/',views.add_tutorials, name='add_tutorials'),
]