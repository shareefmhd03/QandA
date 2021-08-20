from django.urls import path
from . views import *

urlpatterns =[
    path('',view_challenges,name='view_challenges'),
    path('compiler/<int:topic>', code_editor, name = "compiler"),
    path('result/<int:pk>', result, name = "result"),
    path('challenge_quest/<int:topic>', challenge_quest, name = "challenge_quest"),
]