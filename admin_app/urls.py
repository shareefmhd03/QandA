from django.urls import path
from . import views

urlpatterns = [
    path('user_mgmt/',views.user_mgmt, name='user_mgmt'),
    path('add_user/',views.add_user, name='add_user'),
    path('user_unblock/',views.user_unblock, name='user_unblock'),
    path('delete_user/',views.delete_user, name='delete_user'),
    path('view_tutorials/',views.view_tutorials, name='view_tutorials'),
    path('add_tutorials/',views.add_tutorials, name='add_tutorials'),
    path('add_topic/',views.add_topic, name='add_topic'),
    path('add_mcq/',views.add_mcq, name='add_mcq'),
    path('mcqquestions/<int:id>',views.mcqquestions, name='mcqquestions'),
    path('all_topics/',views.all_topics, name='all_topics'),
    path('view_tutorial/<int:id>',views.view_tutorial, name='view_tutorial'),
    path('edit_tutorials/<int:id>',views.edit_tutorials, name='edit_tutorials'),
    path('view_challenges_admin/',views.view_challenges_admin, name='view_challenges_admin'),
    path('add_challenges/',views.add_challenges, name='add_challenges'),
    path('add_challenge_topic/',views.add_challenge_topic, name='add_challenge_topic'),
    path('show_challenge/<int:id>',views.show_challenge, name='show_challenge'),
    path('edit_challenge/<int:id>',views.edit_challenge, name='edit_challenge'),
    path('admin_dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('delete_topic/<int:pk>', views.delete_topic, name = 'delete_topic'),
    path('delete_challenge/<int:pk>', views.delete_challenge, name = 'delete_challenge'),
    path('delete_tutorial/<int:pk>', views.delete_tutorial, name = 'delete_tutorial'),
]