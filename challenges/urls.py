from django.urls import path
from . views import *

urlpatterns =[
    path('',view_challenges,name='view_challenges'),
    path('runcode/',runcode, name="runcode"),
]