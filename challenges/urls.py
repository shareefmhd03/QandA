from django.urls import path
from . views import *

urlpatterns =[
    path('',view_challenges,name='view_challenges'),
    path('compiler/', code_editor, name = "compiler"),
    path('result/', result, name = "result"),
]